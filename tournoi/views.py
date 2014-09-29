from datetime import datetime
from random import randint

from django.shortcuts import render, redirect, get_object_or_404

from tournoi.models import Tournoi, Invit, TournoiForm, Staff, Inscrit, Match, Arbre, DemiFinale, Quart, Huitieme, Seizieme, Trentedeuxieme, Poule
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
    inscrits = Inscrit.objects.filter(tournoi=tournoi).order_by('date')
    if request.user == tournoi.admin or Staff.objects.filter(tournoi=tournoi,admin=request.user) :
        contacts = Contact.objects.filter(owner=Profil.objects.get(u=request.user)).order_by('contact__pseudo')
        membres = Profil.objects.filter(u__is_active=True).order_by('pseudo')
        invites = Invit.objects.filter(tournoi=tournoi).order_by('invite__username')
        staffs = Staff.objects.filter(tournoi=tournoi).order_by('admin__username')
    if Inscrit.objects.filter(tournoi=tournoi,user=request.user):
        inscrit = True
    return render(request,'tournoi/detail.html',{'inscrits':inscrits,'inscrop':inscrop,'inscrit':inscrit,'tournoi':tournoi,'contacts':contacts,'membres':membres,'invites':invites,'staffs':staffs})

def arbre(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi,pk=tournoi_id)
    arbre = list()
    if not Arbre.objects.filter(tournoi=tournoi) and (tournoi.date < datetime.now().date() or (tournoi.date == datetime.now().date() and tournoi.heure <= datetime.now().time())) :
        if Inscrit.objects.filter(tournoi=tournoi) :
            inscrits = Inscrit.objects.filter(tournoi=tournoi)
            for inscrit in inscrits :
                inscrit.order = randint(0,1000000)
                inscrit.save()
            inscrits = list()
            inscritstmp = Inscrit.objects.filter(tournoi=tournoi).order_by('order')
            for insc in inscritstmp :
                inscrits.append(insc.user)
            endinscrits = reversed(inscrits)
            arbre = Arbre.objects.create(tournoi=tournoi)
            if len(inscrits) > 32 :
                trentedeuxieme = Trentedeuxieme.objects.create()
                match1 = Match.objects.create(first=inscrits[0],second=endinscrits[0])
                trentedeuxieme.match1 = match1
                match2 = Match.objects.create(first=inscrits[1])
                if len(inscrits) > 33 :
                    match2.second = endinscrits[1]
                    match2.save()
                trentedeuxieme.match2 = match2
                match3 = Match.objects.create(first=inscrits[2])
                if len(inscrits) > 34 :
                    match3.second = endinscrits[2]
                    match3.save()
                trentedeuxieme.match3 = match3
                match4 = Match.objects.create(first=inscrits[3])
                if len(inscrits) > 35 :
                    match4.second = endinscrits[3]
                    match4.save()
                trentedeuxieme.match4 = match4
                match5 = Match.objects.create(first=inscrits[4])
                if len(inscrits) > 36 :
                    match5.second = endinscrits[4]
                    match5.save()
                trentedeuxieme.match5 = match5
                match6 = Match.objects.create(first=inscrits[5])
                if len(inscrits) > 37 :
                    match6.second = endinscrits[5]
                    match6.save()
                trentedeuxieme.match6 = match6
                match7 = Match.objects.create(first=inscrits[6])
                if len(inscrits) > 38 :
                    match7.second = endinscrits[6]
                    match7.save()
                trentedeuxieme.match7 = match7
                match8 = Match.objects.create(first=inscrits[7])
                if len(inscrits) > 39 :
                    match8.second = endinscrits[7]
                    match8.save()
                trentedeuxieme.match8 = match8
                match9 = Match.objects.create(first=inscrits[8])
                if len(inscrits) > 40 :
                    match9.second = endinscrits[8]
                    match9.save()
                trentedeuxieme.match9 = match9
                match10 = Match.objects.create(first=inscrits[9])
                if len(inscrits) > 41 :
                    match10.second = endinscrits[9]
                    match10.save()
                trentedeuxieme.match10 = match10
                match11 = Match.objects.create(first=inscrits[10])
                if len(inscrits) > 42 :
                    match11.second = endinscrits[10]
                    match11.save()
                trentedeuxieme.match11 = match11
                match12 = Match.objects.create(first=inscrits[11])
                if len(inscrits) > 43 :
                    match12.second = endinscrits[11]
                    match12.save()
                trentedeuxieme.match12 = match12
                match13 = Match.objects.create(first=inscrits[12])
                if len(inscrits) > 44 :
                    match13.second = endinscrits[12]
                    match13.save()
                trentedeuxieme.match13 = match13
                match14 = Match.objects.create(first=inscrits[13])
                if len(inscrits) > 45 :
                    match14.second = endinscrits[13]
                    match14.save()
                trentedeuxieme.match14 = match14
                match15 = Match.objects.create(first=inscrits[14])
                if len(inscrits) > 46 :
                    match15.second = endinscrits[14]
                    match15.save()
                trentedeuxieme.match15 = match15
                match16 = Match.objects.create(first=inscrits[15])
                if len(inscrits) > 47 :
                    match16.second = endinscrits[15]
                    match16.save()
                trentedeuxieme.match16 = match16
                match17 = Match.objects.create(first=inscrits[16])
                if len(inscrits) > 48 :
                    match17.second = endinscrits[16]
                    match17.save()
                trentedeuxieme.match17 = match17
                match18 = Match.objects.create(first=inscrits[17])
                if len(inscrits) > 49 :
                    match18.second = endinscrits[17]
                    match18.save()
                trentedeuxieme.match18 = match18
                match19 = Match.objects.create(first=inscrits[18])
                if len(inscrits) > 50 :
                    match19.second = endinscrits[18]
                    match19.save()
                trentedeuxieme.match19 = match19
                match20 = Match.objects.create(first=inscrits[19])
                if len(inscrits) > 51 :
                    match20.second = endinscrits[19]
                    match20.save()
                trentedeuxieme.match20 = match20
                match21 = Match.objects.create(first=inscrits[20])
                if len(inscrits) > 52 :
                    match21.second = endinscrits[20]
                    match21.save()
                trentedeuxieme.match21 = match21
                match22 = Match.objects.create(first=inscrits[21])
                if len(inscrits) > 53 :
                    match22.second = endinscrits[21]
                    match22.save()
                trentedeuxieme.match22 = match22
                match23 = Match.objects.create(first=inscrits[22])
                if len(inscrits) > 54 :
                    match23.second = endinscrits[22]
                    match23.save()
                trentedeuxieme.match23 = match23
                match24 = Match.objects.create(first=inscrits[23])
                if len(inscrits) > 55 :
                    match24.second = endinscrits[23]
                    match24.save()
                trentedeuxieme.match24 = match24
                match25 = Match.objects.create(first=inscrits[24])
                if len(inscrits) > 56 :
                    match25.second = endinscrits[24]
                    match25.save()
                trentedeuxieme.match25 = match25
                match26 = Match.objects.create(first=inscrits[25])
                if len(inscrits) > 57 :
                    match26.second = endinscrits[25]
                    match26.save()
                trentedeuxieme.match26 = match26
                match27 = Match.objects.create(first=inscrits[26])
                if len(inscrits) > 58 :
                    match27.second = endinscrits[26]
                    match27.save()
                trentedeuxieme.match27 = match27
                match28 = Match.objects.create(first=inscrits[27])
                if len(inscrits) > 59 :
                    match28.second = endinscrits[27]
                    match28.save()
                trentedeuxieme.match28 = match28
                match29 = Match.objects.create(first=inscrits[28])
                if len(inscrits) > 60 :
                    match29.second = endinscrits[28]
                    match29.save()
                trentedeuxieme.match29 = match29
                match30 = Match.objects.create(first=inscrits[29])
                if len(inscrits) > 61 :
                    match30.second = endinscrits[29]
                    match30.save()
                trentedeuxieme.match30 = match30
                match31 = Match.objects.create(first=inscrits[30])
                if len(inscrits) > 62 :
                    match31.second = endinscrits[30]
                    match31.save()
                trentedeuxieme.match31 = match31
                match32 = Match.objects.create(first=inscrits[31])
                if len(inscrits) > 63 :
                    match32.second = endinscrits[31]
                    match32.save()
                trentedeuxieme.match32 = match32
                trentedeuxieme.save()
                arbre.trentedeuxieme = trentedeuxieme
            if len(inscrits) > 16 :
                seizieme = Seizieme.objects.create()
                if len(inscrits) > 32 :
                    match1 = Match.objects.create()
                    seizieme.match1 = match1
                    match2 = Match.objects.create()
                    seizieme.match2 = match2
                    match3 = Match.objects.create()
                    seizieme.match3 = match3
                    match4 = Match.objects.create()
                    seizieme.match4 = match4
                    match5 = Match.objects.create()
                    seizieme.match5 = match5
                    match6 = Match.objects.create()
                    seizieme.match6 = match6
                    match7 = Match.objects.create()
                    seizieme.match7 = match7
                    match8 = Match.objects.create()
                    seizieme.match8 = match8
                    match9 = Match.objects.create()
                    seizieme.match9 = match9
                    match10 = Match.objects.create()
                    seizieme.match10 = match10
                    match11 = Match.objects.create()
                    seizieme.match11 = match11
                    match12 = Match.objects.create()
                    seizieme.match12 = match12
                    match13 = Match.objects.create()
                    seizieme.match13 = match13
                    match14 = Match.objects.create()
                    seizieme.match14 = match14
                    match15 = Match.objects.create()
                    seizieme.match15 = match15
                    match16 = Match.objects.create()
                    seizieme.match16 = match16
                else :
                    match1 = Match.objects.create(first=inscrits[0],second=endinscrits[0])
                    seizieme.match1 = match1
                    match2 = Match.objects.create(first=inscrits[1])
                    if len(inscrits) > 17 :
                        match2.second = endinscrits[1]
                        match2.save()
                    seizieme.match2 = match2
                    match3 = Match.objects.create(first=inscrits[2])
                    if len(inscrits) > 18 :
                        match3.second = endinscrits[2]
                        match3.save()
                    seizieme.match3 = match3
                    match4 = Match.objects.create(first=inscrits[3])
                    if len(inscrits) > 19 :
                        match4.second = endinscrits[3]
                        match4.save()
                    seizieme.match4 = match4
                    match5 = Match.objects.create(first=inscrits[4])
                    if len(inscrits) > 20 :
                        match5.second = endinscrits[4]
                        match5.save()
                    seizieme.match5 = match5
                    match6 = Match.objects.create(first=inscrits[5])
                    if len(inscrits) > 21 :
                        match6.second = endinscrits[5]
                        match6.save()
                    seizieme.match6 = match6
                    match7 = Match.objects.create(first=inscrits[6])
                    if len(inscrits) > 22 :
                        match7.second = endinscrits[6]
                        match7.save()
                    seizieme.match7 = match7
                    match8 = Match.objects.create(first=inscrits[7])
                    if len(inscrits) > 23 :
                        match8.second = endinscrits[7]
                        match8.save()
                    seizieme.match8 = match8
                    match9 = Match.objects.create(first=inscrits[8])
                    if len(inscrits) > 24 :
                        match9.second = endinscrits[8]
                        match9.save()
                    seizieme.match9 = match9
                    match10 = Match.objects.create(first=inscrits[9])
                    if len(inscrits) > 25 :
                        match10.second = endinscrits[9]
                        match10.save()
                    seizieme.match10 = match10
                    match11 = Match.objects.create(first=inscrits[10])
                    if len(inscrits) > 26 :
                        match11.second = endinscrits[10]
                        match11.save()
                    seizieme.match11 = match11
                    match12 = Match.objects.create(first=inscrits[11])
                    if len(inscrits) > 27 :
                        match12.second = endinscrits[11]
                        match12.save()
                    seizieme.match12 = match12
                    match13 = Match.objects.create(first=inscrits[12])
                    if len(inscrits) > 28 :
                        match13.second = endinscrits[12]
                        match13.save()
                    seizieme.match13 = match13
                    match14 = Match.objects.create(first=inscrits[13])
                    if len(inscrits) > 29 :
                        match14.second = endinscrits[13]
                        match14.save()
                    seizieme.match14 = match14
                    match15 = Match.objects.create(first=inscrits[14])
                    if len(inscrits) > 30 :
                        match15.second = endinscrits[14]
                        match15.save()
                    seizieme.match15 = match15
                    match16 = Match.objects.create(first=inscrits[15])
                    if len(inscrits) > 31 :
                        match16.second = endinscrits[15]
                        match16.save()
                    seizieme.match16 = match16
                seizieme.save()
                arbre.seizieme = seizieme
            if len(inscrits) > 8 :
                quart = Huitieme.objects.create()
                if len(inscrits) > 16 :
                    match1 = Match.objects.create()
                    quart.match1 = match1
                    match2 = Match.objects.create()
                    quart.match2 = match2
                    match3 = Match.objects.create()
                    quart.match3 = match3
                    match4 = Match.objects.create()
                    quart.match4 = match4
                    match5 = Match.objects.create()
                    quart.match5 = match5
                    match6 = Match.objects.create()
                    quart.match6 = match6
                    match7 = Match.objects.create()
                    quart.match7 = match7
                    match8 = Match.objects.create()
                    quart.match8 = match8
                else :
                    match1 = Match.objects.create(first=inscrits[0],second=endinscrits[0])
                    quart.match1 = match1
                    match2 = Match.objects.create(first=inscrits[1])
                    if len(inscrits) > 9 :
                        match2.second = endinscrits[1]
                        match2.save()
                    quart.match2 = match2
                    match3 = Match.objects.create(first=inscrits[2])
                    if len(inscrits) > 10 :
                        match3.second = endinscrits[2]
                        match3.save()
                    quart.match3 = match3
                    match4 = Match.objects.create(first=inscrits[3])
                    if len(inscrits) > 11 :
                        match4.second = endinscrits[3]
                        match4.save()
                    quart.match4 = match4
                    match5 = Match.objects.create(first=inscrits[4])
                    if len(inscrits) > 12 :
                        match5.second = endinscrits[4]
                        match5.save()
                    quart.match5 = match5
                    match6 = Match.objects.create(first=inscrits[5])
                    if len(inscrits) > 13 :
                        match6.second = endinscrits[5]
                        match6.save()
                    quart.match6 = match6
                    match7 = Match.objects.create(first=inscrits[6])
                    if len(inscrits) > 14 :
                        match7.second = endinscrits[6]
                        match7.save()
                    quart.match7 = match7
                    match8 = Match.objects.create(first=inscrits[7])
                    if len(inscrits) > 15 :
                        match8.second = endinscrits[7]
                        match8.save()
                    quart.match8 = match8
                quart.save()
                arbre.quart = huitieme
            if len(inscrits) > 4 :
                quart = Quart.objects.create()
                if len(inscrits) > 8 :
                    match1 = Match.objects.create()
                    quart.match1 = match1
                    match2 = Match.objects.create()
                    quart.match2 = match2
                    match3 = Match.objects.create()
                    quart.match3 = match3
                    match4 = Match.objects.create()
                    quart.match4 = match4
                else :
                    match1 = Match.objects.create(first=inscrits[0],second=endinscrits[0])
                    quart.match1 = match1
                    match2 = Match.objects.create(first=inscrits[1])
                    if len(inscrits) > 5 :
                        match2.second = endinscrits[1]
                        match2.save()
                    quart.match2 = match2
                    match3 = Match.objects.create(first=inscrits[2])
                    if len(inscrits) > 6 :
                        match3.second = endinscrits[2]
                        match3.save()
                    quart.match3 = match3
                    match4 = Match.objects.create(first=inscrits[3])
                    if len(inscrits) > 7 :
                        match4.second = endinscrits[3]
                        match4.save()
                    quart.match4 = match4
                quart.save()
                arbre.quart = quart
            if len(inscrits) > 2 :
                demifinale = DemiFinale.objects.create()
                if len(inscrits) > 4 :
                    match1 = Match.objects.create()
                    demifinale.match1 = match1
                    match2 = Match.objects.create()
                    demifinale.match2 = match2
                else :
                    match1 = Match.objects.create(first=inscrits[0],second=endinscrits[0])
                    demifinale.match1 = match1
                    match2 = Match.objects.create(first=inscrits[1])
                    if len(inscrits) > 3 :
                        match2.second = endinscrits[1]
                        match2.save()
                    demifinale.match2 = match2
                demifinale.save()
                arbre.demifinale = demifinale
                petitefinale = Match.objects.create()
                arbre.petitefinale = petitefinale
            finale = Match.objects.create()
            if len(inscrits) <= 2 :
                finale.first = inscrits[0]
                if len(inscrits) == 2 :
                    finale.second = inscrits[1]
                finale.save()
            arbre.finale = finale
            arbre.save()
    elif Arbre.objects.filter(tournoi=tournoi):
        arbre = Arbre.objects.get(tournoi=tournoi)
    return render(request,'tournoi/arbre.html',{'arbre':arbre,'tournoi':tournoi})
                
                    
                    

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

