# -*- encoding:utf-8 -*-
from datetime import datetime
from random import randint

from django.shortcuts import render, redirect, get_object_or_404

from tournoi.models import Tournoi, Invit, TournoiForm, Staff, Inscrit, Match
from profil.models import Profil, Contact
from notification.models import InviteTournoi

from django.contrib.auth.models import User

# Create your views here.

def home_page(request):
    tournoi_open = list()
    for ot in Tournoi.objects.filter(date__gte=datetime.now().date()).order_by('date','heure') :
        if (ot.date == datetime.now().date() and ot.heure >= datetime.now().time()) or ot.date > datetime.now().date() :
            if (ot.prive and request.user.is_active and Invit.objects.filter(tournoi=ot,invite=request.user)) or not ot.prive :
                tournoi_open.append(ot)
    tournoi_en_cours = Tournoi.objects.filter(date__lte=datetime.now().date(),termine=False).exclude(date=datetime.now().date(),heure__gte=datetime.now().time()).order_by('date','heure')
    tournoi_fini = Tournoi.objects.filter(termine=True).order_by('-date','-heure')        
    ladder = Profil.objects.filter(cote__gt=0,u__is_active=True).order_by('-cote')[:40]
    context = {'tournoi_open':tournoi_open,'tournoi_en_cours':tournoi_en_cours,'tournoi_fini':tournoi_fini,'ladder':ladder}
    return render(request,'tournoi/home_page.html', context)

def create(request):
    if not request.user.is_active :
        return redirect('/tournoi/')
    tournoi = TournoiForm()
    edit = False
    if request.method == "POST" :
        tournoi = TournoiForm(request.POST)
        if request.GET.get('id') :
            t = get_object_or_404(Tournoi,pk=request.GET.get('id'))
            if request.user == t.admin or Staff.objects.filter(tournoi=t,admin=request.user) :
                tournoi = TournoiForm(request.POST,instance=t)
                edit = True
        if tournoi.is_valid() and not (tournoi.instance.date < datetime.now().date() or (tournoi.instance.date == datetime.now().date() and tournoi.instance.heure <= datetime.now().time())) : 
            tournoi.save()
            thistournoi = Tournoi.objects.get(id=tournoi.instance.id)
            thistournoi.admin = request.user
            thistournoi.save()
            if thistournoi.prive :
                invit = Invit.objects.create(tournoi=thistournoi,invite=request.user)
            return redirect('/tournoi/detail/%d'%thistournoi.id)
    elif request.GET.get('id') :
        t = get_object_or_404(Tournoi,pk=request.GET.get('id'))
        if request.user == t.admin or Staff.objects.filter(tournoi=t,admin=request.user) :
            tournoi = TournoiForm(instance=t)
            edit = True
    return render(request,'tournoi/create.html',{'tournoi':tournoi,'edit':edit})       

def detail(request,tournoi_id):
    tournoi = get_object_or_404(Tournoi,pk=tournoi_id)
    if request.GET.get('seen') :
        it = InviteTournoi.objects.get(pk=request.GET.get('seen'))
        it.seen = True
        it.save()
    if request.method == "POST" :
        if not request.user.is_active :
            return redirect('/tournoi/detail/%d'%tournoi.id)
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
    staffs = Staff.objects.filter(tournoi=tournoi).order_by('admin__username')
    inscrit = False
    inscrits = Inscrit.objects.filter(tournoi=tournoi).order_by('date')[:tournoi.max_participants]
    attente = Inscrit.objects.filter(tournoi=tournoi).order_by('date')[tournoi.max_participants:]
    if request.user.is_active :
        if request.user == tournoi.admin or Staff.objects.filter(tournoi=tournoi,admin=request.user) :
            contacts = Contact.objects.filter(owner=Profil.objects.get(u=request.user)).order_by('contact__pseudo')
            membres = Profil.objects.filter(u__is_active=True).order_by('pseudo')
            invites = Invit.objects.filter(tournoi=tournoi).order_by('invite__username')
        if Inscrit.objects.filter(tournoi=tournoi,user=request.user):
            inscrit = True
    return render(request,'tournoi/detail.html',{'inscrits':inscrits,'inscrop':inscrop,'inscrit':inscrit,'tournoi':tournoi,'contacts':contacts,'membres':membres,'invites':invites,'staffs':staffs,'attente':attente})

def feed_match(tournoi,inscrits=list(),indice=0,total=0,next_gagnant=False,next_perdant=False):
    match = Match.objects.create(tournoi=tournoi,col=total,row=indice)
    if len(inscrits) :
        match.first = inscrits[indice].user
        if len(inscrits) > indice + total :
            match.second = inscrits[indice+total].user
        else :
            match.freewin = True
    if next_gagnant :
        match.next_gagnant = next_gagnant
    if next_perdant :
        match.next_perdant = next_perdant
    match.save()
    return match

def arbre(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi,pk=tournoi_id)
    #Génération de l'arbre
    if not Match.objects.filter(tournoi=tournoi) and (tournoi.date < datetime.now().date() or (tournoi.date == datetime.now().date() and tournoi.heure <= datetime.now().time())) :
        #Génération de la liste des inscrits
        inscrits = Inscrit.objects.filter(tournoi=tournoi).order_by('date')[:tournoi.max_participants]
        for inscrit in inscrits :
            inscrit.order = randint(1,1000000)
            inscrit.save()
        inscrits = Inscrit.objects.filter(tournoi=tournoi).order_by('-order')[:tournoi.max_participants]
        if len(inscrits) <= 1 :
            tournoi.termine = True
            if inscrits :
                tournoi.vainqueur = inscrits[0].user
            tournoi.save()
        else :
            inscr = list()
            if len(inscrits) <= 2 :
                inscr = inscrits
            finale = feed_match(tournoi,inscr)
            if len(inscrits) > 2 :
                if len(inscrits) <= 4 :
                    inscr = inscrits
                petite_finale = feed_match(tournoi,indice=1)
                demifinale1 = feed_match(tournoi,inscr,0,2,finale,petite_finale)
                demifinale2 = feed_match(tournoi,inscr,1,2,finale,petite_finale)
            if len(inscrits) > 4 :
                if len(inscrits) <= 8 :
                    inscr = inscrits
                quart1 = feed_match(tournoi,inscr,0,4,demifinale1)
                quart2 = feed_match(tournoi,inscr,1,4,demifinale1)
                quart3 = feed_match(tournoi,inscr,2,4,demifinale2)
                quart4 = feed_match(tournoi,inscr,3,4,demifinale2)
            if len(inscrits) > 8 :
                if len(inscrits) <= 16 :
                    inscr = inscrits
                huitieme1 = feed_match(tournoi,inscr,0,8,quart1)
                huitieme2 = feed_match(tournoi,inscr,1,8,quart1)
                huitieme3 = feed_match(tournoi,inscr,2,8,quart2)
                huitieme4 = feed_match(tournoi,inscr,3,8,quart2)
                huitieme5 = feed_match(tournoi,inscr,4,8,quart3)
                huitieme6 = feed_match(tournoi,inscr,5,8,quart3)
                huitieme7 = feed_match(tournoi,inscr,6,8,quart4)
                huitieme8 = feed_match(tournoi,inscr,7,8,quart4)
            if len(inscrits) > 16 :
                inscr = inscrits
                seizieme1 = feed_match(tournoi,inscr,0,16,huitieme1)
                seizieme2 = feed_match(tournoi,inscr,1,16,huitieme1)
                seizieme3 = feed_match(tournoi,inscr,2,16,huitieme2)
                seizieme4 = feed_match(tournoi,inscr,3,16,huitieme2)
                seizieme5 = feed_match(tournoi,inscr,4,16,huitieme3)
                seizieme6 = feed_match(tournoi,inscr,5,16,huitieme3)
                seizieme7 = feed_match(tournoi,inscr,6,16,huitieme4)
                seizieme8 = feed_match(tournoi,inscr,7,16,huitieme4)
                seizieme9 = feed_match(tournoi,inscr,8,16,huitieme5)
                seizieme10 = feed_match(tournoi,inscr,9,16,huitieme5)
                seizieme11 = feed_match(tournoi,inscr,10,16,huitieme6)
                seizieme12 = feed_match(tournoi,inscr,11,16,huitieme6)
                seizieme13 = feed_match(tournoi,inscr,12,16,huitieme7)
                seizieme14 = feed_match(tournoi,inscr,13,16,huitieme7)
                seizieme15 = feed_match(tournoi,inscr,14,16,huitieme8)
                seizieme16 = feed_match(tournoi,inscr,15,16,huitieme8)
            while Match.objects.filter(freewin=True,valide=False) :
                for m in Match.objects.filter(freewin=True,valide=False) :
                    if m.next_gagnant :
                        next_m = m.next_gagnant
                        if not next_m.first :
                            next_m.first = m.first
                        else :
                            next_m.second = m.first
                        next_m.save()
                    m.valide = True
                    m.save()
    arbre = Match.objects.filter(tournoi=tournoi).order_by('-col','row')
    try :
        next_match = Match.objects.get(tournoi=tournoi,first=request.user,valide=False)
    except :
        try :
            next_match = Match.objects.get(tournoi=tournoi,second=request.user,valide=False)
        except :
            next_match = False
    if request.GET.get('error') :
        error_msg = request.GET.get('error')
    else :
        error_msg = str()
    admin = list()
    if request.user.is_active :
        admin = Staff.objects.filter(tournoi=tournoi,admin=request.user)
    return render(request,'tournoi/arbre.html',{'arbre':arbre,'tournoi':tournoi,'next_match':next_match,'error_msg':error_msg,'admin':admin})

def feed_freewin(go,dego):
    while go or dego :
        for let in go :
            let1 = let[1]
            let = let[0]
            let.first = let1
            let.valide = True
            let.save()
            if let.next_gagnant : 
                if let.next_gagnant.freewin :
                    go.append([let.next_gagnant,let.first])
                else :
                    n_g = let.next_gagnant
                    if n_g.first :
                        n_g.second = let1
                    else :
                        n_g.first = let1
                    n_g.save()

            if let.next_perdant and let.next_perdant.freewin :
                dego.append(let.next_perdant)
                
            tournoi = let.tournoi
            if let.col == 0 and not Match.objects.filter(tournoi=tournoi,col=0,score__isnull=True).exclude(freewin=True):
                tournoi.termine = True
                tournoi.save()
            
            if let.col == 0 and let.row == 0 :
                tournoi.vainqueur = let1
                tournoi.save()
                cote = Profil.objects.get(u=let1)
                if tournoi.loser_bracket :
                    multiple = 5
                else :
                    multiple = 10
                cote.cote += multiple*len(Match.objects.filter(tournoi=tournoi))
                cote.save()
            go.remove([let,let.first])
        for let in dego :
            if let.freewin :
                let.valide = True
            else :
                let.freewin = True
            let.save()
            tournoi = let.tournoi
            if let.col == 0 and not Match.objects.filter(tournoi=tournoi,col=0,score__isnull=True).exclude(freewin=True):
                tournoi.termine = True
                tournoi.save()
            if let.next_gagnant :
                if let.next_gagnant.freewin :
                    dego.append(let.next_gagnant)
                else :
                    gagnant = let.next_gagnant
                    gagnant.freewin = True
                    if let.next_gagnant.first :
                        go.append([let.next_gagnant,let.next_gagnant.first])
                        gagnant.valide = True
                    gagnant.save()
            if let.next_perdant :
                if let.next_perdant.freewin :
                    dego.append(let.next_perdant)
                else :   
                    perdant = let.next_perdant
                    perdant.freewin = True
                    if let.next_perdant.first :
                        go.append([let.next_perdant,let.next_perdant.first])
                        perdant.valide=True
                    perdant.save()
            dego.remove(let)
    return True

def u_s(match,score):
    match.score = int(score)
    match.valide = True
    match.save()
    if int(score[0]) > int(score[1]) :
        vainqueur = match.first
        perdant = match.second
    else :
        vainqueur = match.second
        perdant = match.first
    if match.col == 0 and match.row == 0 :
        tournoi = match.tournoi
        tournoi.vainqueur = vainqueur
        tournoi.save()
        cote = Profil.objects.get(u=vainqueur)
        if tournoi.loser_bracket :
            multiple = 5
        else :
            multiple = 10
        cote.cote += multiple*len(Match.objects.filter(tournoi=tournoi))
        cote.save()
    if match.next_gagnant :
        if match.next_gagnant.freewin :
            ff = feed_freewin([[match.next_gagnant,vainqueur]],[])               
                                
        else :
            n_g = match.next_gagnant
            if n_g.first :
                n_g.second = vainqueur
            else :
                n_g.first = vainqueur
            n_g.save()
    if match.next_perdant :
        if match.next_perdant.freewin :
            ff = feed_freewin([[match.next_perdant,perdant]],[])               
        else :
            n_p = match.next_perdant
            if n_p.first :
                n_p.second = perdant
            else :
                n_p.first = perdant
            n_p.save()
    return match

def cote(user1,user2,diff):
    cote1 = float(user1.cote)
    cote2 = float(user2.cote)
    if diff > 0 :
        indice = ((cote2*100)/cote1)/2
    else :
        indice = ((cote1*100)/cote2)/2
    if indice > 100 :
        indice = 100
    if diff > 0 :
        result1 = cote1+(indice*diff)
        result2 = cote2-(indice*diff)
    else :
        result1 = cote1-(indice*-diff)
        result2 = cote2+(indice*-diff)
    if result1 <= 0 :
        result1 = 1
    if result2 <= 0 :
        result2 = 1
    user1.cote = int(result1)
    user2.cote = int(result2)
    user1.save()
    user2.save()
    return True
                
def update_score(request,match_id):
    match = get_object_or_404(Match,pk=match_id)
    if not request.user.is_active :
        return redirect('/tournoi/arbre/%d'%match.tournoi.id)
    error_msg = u''
    if not match.valide and request.method == "POST" :
        try :
            request.POST['freewin']
            match.freewin = True
            match.valide = True
            match.score = "00"
            match.save()
            ff = feed_freewin([],[match])
        except :
            score = str(request.POST['sc_f'])+str(request.POST['sc_s'])
            if match.col == 0 :
                result = match.tournoi.finale
            else :
                result = match.tournoi.match
            try :
                int(score)
            except :
                score = ""
            if len(score) != 2 or (score[0] == score[1] or (int(score[0]) !=  result and int(score[1]) != result)) :
                error_msg = "invalide"
            else :
                admins = Staff.objects.filter(tournoi=match.tournoi)
                if request.user == match.tournoi.admin or request.user in admins :
                    confirmed = u_s(match,score)
                    user1 = match.first.profil_set.all()[0]
                    user2 = match.second.profil_set.all()[0]
                    define_cote = cote(user1,user2,int(score[0])-int(score[1]))
                    if match.col == 0 and not Match.objects.filter(tournoi=match.tournoi,col=0,score__isnull=True).exclude(freewin=True) :
                        tournoi = match.tournoi
                        tournoi.termine = True
                        tournoi.save()
                elif request.user in [match.first,match.second] :
                    if request.user == match.first :
                        first = True
                    else :
                        first = False
                    if (first and match.score_second == score) or (not first and match.score_first == score) :
                        confirmed = u_s(match,score)
                        user1 = match.first.profil_set.all()[0]
                        user2 = match.second.profil_set.all()[0]
                        define_cote = cote(user1,user2,int(score[0])-int(score[1]))
                        if match.col == 0 and not Match.objects.filter(tournoi=match.tournoi,col=0,score__isnull=True).exclude(freewin=True):
                            tournoi = match.tournoi
                            tournoi.termine = True
                            tournoi.save()
                    elif first and not match.score_second :
                        match.score_first = score
                        match.save()
                    elif not first and not match.score_first :
                        match.score_second = score
                        match.save()
                    elif first :
                        match.score_first = score
                        match.save()
                        error_msg="dismatch"
                    else :
                        match.score_second = score
                        match.save()
                        error_msg="dismatch"
                    
    return  redirect(u'/tournoi/arbre/%d?error=%s'%(match.tournoi.id,error_msg))
                    

def inscription(request,tournoi_id):
    tournoi = get_object_or_404(Tournoi,pk=tournoi_id)
    if request.user.is_active :
        if (tournoi.prive and Invit.objects.filter(tournoi=tournoi,invite=request.user)) or not tournoi.prive :
            inscrit = Inscrit.objects.create(tournoi=tournoi,user=request.user)
            tournoi.inscrit += 1
            tournoi.save()
    return redirect('/tournoi/detail/%d'%tournoi.id) 

def desinscription(request,tournoi_id):
    tournoi = get_object_or_404(Tournoi,pk=tournoi_id)
    if request.user.is_active :
        inscr = Inscrit.objects.get(tournoi=tournoi,user=request.user)
        inscr.delete()
        tournoi.inscrit -= 1
        tournoi.save()
    return redirect('/tournoi/detail/%d'%tournoi.id) 

