from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404

from tournoi.models import Tournoi, Invit, TournoiForm, Staff, Inscrit
from profil.models import Profil, Contact
from notification.models import InviteTournoi

from django.contrib.auth.models import User

# Create your views here.

def home_page(request):
    tournoi_open = list()
    for ot in Tournoi.objects.filter(date__gte=datetime.now().date()).order_by('date').order_by('heure') :
        if (ot.date == datetime.now().date() and ot.heure >= datetime.now().time()) or ot.date > datetime.now().date() :
            if (ot.prive and request.user.is_active and Invit.objects.filter(tournoi=ot,invite=request.user)) or not ot.prive :
                tournoi_open.append(ot)
    tournoi_en_cours = Tournoi.objects.filter(date__lte=datetime.now().date(),heure__lte=datetime.now().time(),termine=False).order_by('date').order_by('heure')
    tournoi_fini = Tournoi.objects.filter(termine=True).order_by('date').order_by('heure')        
    context = {'tournoi_open':tournoi_open,'tournoi_en_cours':tournoi_en_cours,'tournoi_fini':tournoi_fini}
    return render(request,'tournoi/home_page.html', context)

def create(request):
    if request.method == "POST" :
        tournoi = TournoiForm(request.POST)
        if tournoi.is_valid():
            tournoi.save()
            thistournoi = Tournoi.objects.all().order_by('-id')[0]
            thistournoi.admin = request.user
            thistournoi.save()
            if thistournoi.prive :
                invit = Invit.objects.create(tournoi=thistournoi,invite=request.user)
            return redirect('/tournoi/detail/%d'%thistournoi.id)
    else :
        tournoi = TournoiForm()
    return render(request,'tournoi/create.html',{'tournoi':tournoi})       

def detail(request,tournoi_id):
    tournoi = get_object_or_404(Tournoi,pk=tournoi_id)
    if request.GET.get('seen') :
        it = InviteTournoi.objects.get(pk=request.GET.get('seen'))
        it.seen = True
        it.save()
    if request.method == "POST" :
        if request.POST['action'] == "staff" :
            for staff in Staff.objects.filter(tournoi=tournoi):
                notif = InviteTournoi.objects.get(user=staff.admin,staff=True,tournoi=tournoi)
                notif.delete()
                staff.delete()
            for staff in request.POST['staff'].split(" "):
                if User.objects.filter(username=staff) and not Staff.objects.filter(tournoi=tournoi,admin=User.objects.get(username=staff)):
                    new_staff = Staff.objects.create(tournoi=tournoi,admin=User.objects.get(username=staff))
                    if not InviteTournoi.objects.filter(user=User.objects.get(username=staff),staff=True,tournoi=tournoi):
                        it = InviteTournoi.objects.create(user=User.objects.get(username=staff),staff=True,tournoi=tournoi)
                    
        if request.POST['action'] == "invite" :
            for invit in Invit.objects.filter(tournoi=tournoi):
                notif = InviteTournoi.objects.get(user=invit.invite,staff=False,tournoi=tournoi)
                notif.delete()
                invit.delete()
            for invit in request.POST["invit"].split(" "):
                if User.objects.filter(username=invit) and not Invit.objects.filter(tournoi=tournoi,invite=User.objects.get(username=invit)):
                    new_invit = Invit.objects.create(tournoi=tournoi,invite=User.objects.get(username=invit))
                    if not InviteTournoi.objects.filter(user=User.objects.get(username=invit),staff=False,tournoi=tournoi):
                        it = InviteTournoi.objects.create(user=User.objects.get(username=invit),tournoi=tournoi)
    inscrop = False
    if tournoi.date > datetime.now().date() or (tournoi.date == datetime.now().date() and tournoi.heure > datetime.now().time()) :
        inscrop = True
    contacts = list()
    membres = list()
    invites = list()
    staffs = list()
    inscrit = False
    if request.user == tournoi.admin or Staff.objects.filter(tournoi=tournoi,admin=request.user) :
        contacts = Contact.objects.filter(owner=Profil.objects.get(u=request.user)).order_by('contact__pseudo')
        membres = Profil.objects.filter(u__is_active=True).order_by('pseudo')
        invites = Invit.objects.filter(tournoi=tournoi).order_by('invite__username')
        staffs = Staff.objects.filter(tournoi=tournoi).order_by('admin__username')
        if Inscrit.objects.filter(tournoi=tournoi,user=request.user):
            inscrit = True
    return render(request,'tournoi/detail.html',{'inscrop':inscrop,'inscrit':inscrit,'tournoi':tournoi,'contacts':contacts,'membres':membres,'invites':invites,'staffs':staffs})

def inscription(request,tournoi_id):
    tournoi = get_object_or_404(Tournoi,pk=tournoi_id)
    if (tournoi.prive and Invit.objects.filter(tournoi=tournoi,invite=request.user)) or not tournoi.prive :
        inscrit = Inscrit.objects.create(tournoi=tournoi,user=request.user)
        tournoi.inscrit += 1
        tournoi.save()
    return redirect('/tournoi/detail/%d'%tournoi.id) 

def desinscription(request,tournoi_id):
    tournoi = get_object_or_404(Tournoi,pk=tournoi_id)
    inscr = Inscrit.objects.get(tournoi=tournoi,user=request.user)
    inscr.delete()
    tournoi.inscrit -= 1
    tournoi.save()
    return redirect('/tournoi/detail/%d'%tournoi.id) 
