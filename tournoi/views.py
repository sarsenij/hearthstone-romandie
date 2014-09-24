from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404

from tournoi.models import Tournoi, Invit, TournoiForm

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
    return render(request,'tournoi/detail.html',{'tournoi':tournoi})
