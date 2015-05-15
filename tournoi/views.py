# -*- encoding:utf-8 -*-
from datetime import datetime, date
from random import randint

from django.shortcuts import render, redirect, get_object_or_404

from tournoi.models import Tournoi, Invit, TournoiForm, Inscrit, Match, Duel
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
    tournoi_fini = Tournoi.objects.filter(termine=True).order_by('-date','-heure')[:20] 
    ladder = Profil.objects.filter(cote__gt=0,u__is_active=True,cote_launch=True).order_by('-cote')[:40]
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
            if request.user == t.admin :
                tournoi = TournoiForm(request.POST,instance=t)
                edit = True
        if tournoi.is_valid() and not (tournoi.instance.date < datetime.now().date() or (tournoi.instance.date == datetime.now().date() and tournoi.instance.heure <= datetime.now().time())) : 
            tournoi.save()
            thistournoi = Tournoi.objects.get(id=tournoi.instance.id)
            thistournoi.admin = request.user
            thistournoi.save()
            if thistournoi.prive :
                invit = Invit.objects.create(tournoi=thistournoi,invite=request.user)
                invitourn = InviteTournoi.objects.create(tournoi=thistournoi,user=request.user,staff=False)
            return redirect('/tournoi/detail/%d'%thistournoi.id)
        else :
            tournoi.errors['perime'] = ""
    elif request.GET.get('id') :
        t = get_object_or_404(Tournoi,pk=request.GET.get('id'))
        if request.user == t.admin :
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
                    
        if request.POST['action'] == "invite" :
            for invit in request.POST["invit"].split(" "):
                if User.objects.filter(username=invit) and not Invit.objects.filter(tournoi=tournoi,invite=User.objects.get(username=invit)):
                    new_invit = Invit.objects.create(tournoi=tournoi,invite=User.objects.get(username=invit))
                    if not InviteTournoi.objects.filter(user=User.objects.get(username=invit),staff=False,tournoi=tournoi):
                        it = InviteTournoi.objects.create(user=User.objects.get(username=invit),tournoi=tournoi)
            for invit in Invit.objects.filter(tournoi=tournoi) :
                if invit.invite.username not in request.POST["invit"].split(" "):
                    invit.delete()
                    it = InviteTournoi.objects.get(user=invit.invite,tournoi=tournoi)
                    it.delete()     
            
    inscrop = False
    if tournoi.date > datetime.now().date() or (tournoi.date == datetime.now().date() and tournoi.heure > datetime.now().time()) :
        inscrop = True
    contacts = list()
    membres = list()
    invites = list()
    inscrit = False
    inscrits = Inscrit.objects.filter(tournoi=tournoi).order_by('date')[:tournoi.max_participants]
    attente = Inscrit.objects.filter(tournoi=tournoi).order_by('date')[tournoi.max_participants:]
    if request.user.is_active :
        if request.user == tournoi.admin :
            contacts = Contact.objects.filter(owner=Profil.objects.get(u=request.user)).order_by('contact__pseudo')
            membres = Profil.objects.filter(u__is_active=True).order_by('pseudo')
            invites = Invit.objects.filter(tournoi=tournoi).order_by('invite__username')
        if Inscrit.objects.filter(tournoi=tournoi,user=request.user):
            inscrit = True
    return render(request,'tournoi/detail.html',{'inscrits':inscrits,'inscrop':inscrop,'inscrit':inscrit,'tournoi':tournoi,'contacts':contacts,'membres':membres,'invites':invites,'attente':attente})

def feed_match(tournoi,inscrits=list(),indice=0,total=1,next_gagnant=False,next_perdant=False,poule=False,feed_blank=False):
    match = Match.objects.create(tournoi=tournoi,col=total,row=indice)
    if next_gagnant :
        match.next_gagnant = next_gagnant
    if next_perdant :
        match.next_perdant = next_perdant
    if poule :
        match.poule = poule
    if feed_blank :
        match.freewin = True
        next_gagnant = match.next_gagnant
        next_gagnant.freewin=True
        next_gagnant.save()
        if match.next_perdant :
            next_gagnant = match.next_perdant
            next_gagnant.freewin=True
            next_gagnant.save()
    if len(inscrits) :
        if poule :
            if len(inscrits) >= indice+1 :
                match.first = inscrits[indice].user
            else :
                match.freewin = True
                next_gagnant = match.next_gagnant
                next_gagnant.freewin=True
                next_gagnant.save()
                if match.next_perdant :
                    next_gagnant = match.next_perdant
                    next_gagnant.freewin=True
                    next_gagnant.save()
            if len(inscrits) >= indice+2 :
                match.second = inscrits[indice+1].user
            else :
                match.freewin = True
                next_gagnant = match.next_gagnant
                next_gagnant.freewin=True
                next_gagnant.save()
                if match.next_perdant :
                    next_gagnant = match.next_perdant
                    next_gagnant.freewin=True
                    next_gagnant.save()
        else :
            match.first = inscrits[indice].user
            if len(inscrits) > indice + total :
                match.second = inscrits[indice+total].user
            else :
                match.freewin = True
    match.save()
    return match

def arbre(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi,pk=tournoi_id)
    if request.method == "POST" :
        match = get_object_or_404(Match,pk=request.POST['match'])
        deck = request.POST['deck'] 
        if match.poule :
            manche = tournoi.poules
        elif match.col == 1 :
            manche = tournoi.finale
        else :
            manche = tournoi.match
        if len(deck) != manche :
            error_msg = "deck"
        else :
            if request.user == match.first :
                match.first_deck = deck
            elif request.user == match.second :
                match.second_deck = deck
            if match.first_deck and match.second_deck :
                match.conquest_check = True
            match.save()
    try :
        if request.GET['regenarbre'] == 'y' and request.user == tournoi.admin :
            for match in Match.objects.filter(tournoi=tournoi) :
                match.delete()
            for inscr in Inscrit.objects.filter(tournoi=tournoi) :
                inscr.order = 0
                inscr.save()
    except :
        pass
    #Génération de l'arbre
    if not Match.objects.filter(tournoi=tournoi) and (tournoi.date < datetime.now().date() or (tournoi.date == datetime.now().date() and tournoi.heure <= datetime.now().time())) :
        #Génération de la liste des inscrits
        inscrits = Inscrit.objects.filter(tournoi=tournoi).order_by('date')[:tournoi.max_participants]
        if tournoi.poules :
            inscrits=inscrits[0:len(inscrits)-(len(inscrits)%4)]
        for inscrit in inscrits :
            inscrit.order = randint(1,1000000)
            inscrit.save()
        inscrits = Inscrit.objects.filter(tournoi=tournoi).order_by('-order')[:tournoi.max_participants]
        if tournoi.poules :
            inscrits=inscrits[0:len(inscrits)-(len(inscrits)%4)]
        if len(inscrits) <= 1 :
            tournoi.termine = True
            if inscrits :
                tournoi.vainqueur = inscrits[0].user
            tournoi.save()
        elif len(inscrits) < 8 and tournoi.poules :
            tournoi.termine = True
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
            if len(inscrits) > 4 and (not tournoi.poules or len(inscrits) > 8):
                if len(inscrits) <= 8 and not tournoi.poules:
                    inscr = inscrits
                quart1 = feed_match(tournoi,inscr,0,4,demifinale1)
                quart2 = feed_match(tournoi,inscr,1,4,demifinale1)
                quart3 = feed_match(tournoi,inscr,2,4,demifinale2)
                quart4 = feed_match(tournoi,inscr,3,4,demifinale2)
            if len(inscrits) > 8 and not tournoi.poules or len(inscrits) > 16:
                if len(inscrits) <= 16 and not tournoi.poules:
                    inscr = inscrits
                huitieme1 = feed_match(tournoi,inscr,0,8,quart1)
                huitieme2 = feed_match(tournoi,inscr,1,8,quart1)
                huitieme3 = feed_match(tournoi,inscr,2,8,quart2)
                huitieme4 = feed_match(tournoi,inscr,3,8,quart2)
                huitieme5 = feed_match(tournoi,inscr,4,8,quart3)
                huitieme6 = feed_match(tournoi,inscr,5,8,quart3)
                huitieme7 = feed_match(tournoi,inscr,6,8,quart4)
                huitieme8 = feed_match(tournoi,inscr,7,8,quart4)
            if len(inscrits) > 16 and not tournoi.poules:
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
            if tournoi.poules : 
                if len(inscrits) == 8 :
                    gagnant = [demifinale1,demifinale2]
                    list_inscrit = [inscrits[0:4],inscrits[4:8]]
                elif len(inscrits) <= 16 :
                    gagnant = [quart1,quart2,quart3,quart4]
                    list_inscrit = [inscrits[0:4],inscrits[4:8],inscrits[8:12]]
                    if len(inscrits) > 12 :
                        list_inscrit.append(inscrits[12:16])
                else :
                    gagnant = [huitieme1,huitieme2,huitieme3,huitieme4,huitieme5,huitieme6,huitieme7,huitieme8]
                    list_inscrit = [inscrits[0:4],inscrits[4:8],inscrits[8:12],inscrits[12:16],inscrits[16:20]]
                    if len(inscrits) > 20 :
                        list_inscrit.append(inscrits[20:24])
                    if len(inscrits) > 24 :
                        list_inscrit.append(inscrits[24:28])
                    if len(inscrits) > 28 :
                        list_inscrit.append(inscrits[28:32])
                globalincr = 1
                incr = 0
                for g in gagnant :
                    if globalincr%2 :
                        incr += 1
                    inscr = list()
                    if globalincr%2 :
                        c1 = feed_match(tournoi,inscr,0,1,gagnant[incr-1],poule=globalincr)
                        b1 = feed_match(tournoi,inscr,0,2,gagnant[(len(gagnant)/2)+incr-1],c1,poule=globalincr)
                    else :
                        c1 = feed_match(tournoi,inscr,0,1,gagnant[(len(gagnant)/2)+incr-1],poule=globalincr)
                        b1 = feed_match(tournoi,inscr,0,2,gagnant[incr-1],c1,poule=globalincr)
                    b2 = feed_match(tournoi,inscr,2,2,c1,poule=globalincr)
                    try :
                        li = list_inscrit[globalincr-1]
                        a1 = feed_match(tournoi,li,0,4,b1,b2,poule=globalincr)
                        a2 = feed_match(tournoi,li,2,4,b1,b2,poule=globalincr) 
                    except :
                        a1 = feed_match(tournoi,list(),0,4,b1,b2,poule=globalincr,feed_blank=True)
                        a2 = feed_match(tournoi,list(),2,4,b1,b2,poule=globalincr,feed_blank=True)

                    
                    globalincr += 1
                    
            while Match.objects.filter(tournoi=tournoi,freewin=True,valide=False) :
                for m in Match.objects.filter(tournoi=tournoi,freewin=True,valide=False) :
                    if m.next_gagnant:
                        next_m = m.next_gagnant
                        if not next_m.first :
                            next_m.first = m.first
                        else :
                            next_m.second = m.first
                        next_m.save()
                    m.valide = True
                    m.save()
                        





    arbre = Match.objects.filter(tournoi=tournoi,poule=0,loser_bracket=False).order_by('-col','row')
    poules = Match.objects.filter(tournoi=tournoi,loser_bracket=False).exclude(poule=0).order_by('poule','-col','row')
    try :
        next_match = Match.objects.get(tournoi=tournoi,first=request.user,valide=False)
    except :
        try :
            next_match = Match.objects.get(tournoi=tournoi,second=request.user,valide=False)
        except :
            next_match = False
    if next_match and tournoi.conquest and not next_match.conquest_check:
        conquest = True
    else :
        conquest = False
    if request.GET.get('error') :
        error_msg = request.GET.get('error')
    try :
        error_msg
    except :
        error_msg = str()
    admin = list()
    return render(request,'tournoi/arbre.html',{'arbre':arbre,'poules':poules,'tournoi':tournoi,'next_match':next_match,'error_msg':error_msg,'conquest':conquest})

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

            if let.next_perdant : 
                if let.next_perdant.freewin :
                    dego.append(let.next_perdant)
                
            tournoi = let.tournoi
            if let.col == 1 and not Match.objects.filter(tournoi=tournoi,col=1,score__isnull=True).exclude(freewin=True):
                tournoi.termine = True
                tournoi.save()
            
            if let.col == 1 and let.row == 0 :
                tournoi.vainqueur = let1
                tournoi.save()
                cote = Profil.objects.get(u=let1)
                multiple = 5
                if len(Match.objects.filter(tournoi=Tournoi)) > 3 :
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
            if let.col == 1 and not Match.objects.filter(tournoi=tournoi,col=1,score__isnull=True).exclude(freewin=True):
                tournoi.termine = True
                tournoi.save()
            if let.next_gagnant :
                if let.next_gagnant.freewin :
                    dego.append(let.next_gagnant)
                else :
                    gagnant = let.next_gagnant
                    gagnant.freewin = True
                    if gagnant.next_perdant :
                        dego.append(gagnant.next_perdant)
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
                    if perdant.next_perdant :
                        dego.append(perdant.next_perdant)
                    if let.next_perdant.first :
                        go.append([let.next_perdant,let.next_perdant.first])
                        perdant.valide=True
                    perdant.save()
            dego.remove(let)
    return True

def u_s(match,score):
    match.score = score
    match.valide = True
    match.save()
    if int(score[0]) > int(score[1]) :
        vainqueur = match.first
        perdant = match.second
    else :
        vainqueur = match.second
        perdant = match.first
    if match.col == 1 and match.row == 0 :
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

def cote(user1,user2,diff,ind=100):
    cote1 = float(user1.cote)
    cote2 = float(user2.cote)
    if diff > 0 :
        indice = ((cote2*ind)/cote1)/2
    else :
        indice = ((cote1*ind)/cote2)/2
    if indice > ind :
        indice = ind
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
    user1.cote_launch = True
    user2.cote = int(result2)
    user2.cote_launch = True
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
            if match.poule :
                result = match.tournoi.poules
            elif match.col == 1 :
                result = match.tournoi.finale
            else :
                result = match.tournoi.match
            try :
                int(score)
            except :
                score = ""
            if match.col == 1 :
                attendu = match.tournoi.finale
            else :
                attendu = match.tournoi.match
            if len(score) != 2 or (score[0] == score[1] or (int(score[0]) !=  result and int(score[1]) != result)) or int(score[0]) > attendu or int(score[1]) > attendu :
                error_msg = "invalide"
            else :
                if request.user == match.tournoi.admin :
                    confirmed = u_s(match,score)
                    user1 = match.first.profil_set.all()[0]
                    user2 = match.second.profil_set.all()[0]
                    define_cote = cote(user1,user2,int(score[0])-int(score[1]))
                    if match.col == 1 and not Match.objects.filter(tournoi=match.tournoi,col=1,score__isnull=True).exclude(freewin=True) :
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
                        if match.col == 1 and not Match.objects.filter(tournoi=match.tournoi,col=1,score__isnull=True).exclude(freewin=True):
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
        if request.method == "POST" :
            profil = get_object_or_404(Profil,u=request.user)
            profil.battletag = request.POST['battletag']
            profil.save()
        if (tournoi.prive and Invit.objects.filter(tournoi=tournoi,invite=request.user)) or not tournoi.prive :
            if not Profil.objects.get(u=request.user).battletag :
                return redirect('/tournoi/arbre/%d?error=battletag'%tournoi.id)
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

def launch(request,tournoi_id):
    tournoi = get_object_or_404(Tournoi,pk=tournoi_id)
    if request.user == tournoi.admin :
        tournoi.date = date.today()
        tournoi.heure = datetime.now().strftime('%H:%M')
        tournoi.save()
    return redirect('/tournoi/arbre/%s'%tournoi_id)

def duel_deny(request) :
    if request.method == "POST" :
        duel = get_object_or_404(Duel,pk=request.POST['duel'])
        if duel.first == request.user or duel.second == request.user :
            duel.valide = True
            duel.save()
    return redirect('/')

def duel_score(request,duel_id):
    if request.method == "POST" :
        duel = get_object_or_404(Duel,pk=duel_id)
        if duel.first == request.user :
            duel.first_score = int(request.POST['win'])
        elif duel.second == request.user :
            duel.second_score = int(request.POST['win'])
        duel.save()
        if duel.first_score and duel.first_score == duel.second_score:
            cote(Profil.objects.get(u=duel.first),Profil.objects.get(u=duel.second),duel.first_score-2,10)
            duel.valide = True
        duel.save()
    return redirect('/')
            
def duel_declare(request):
    if request.method == "POST" :
        profil = get_object_or_404(Profil,u=request.user)
        adversaire = get_object_or_404(Profil,pk=request.POST['adversaire'])
        if profil.battletag and adversaire.battletag and not Duel.objects.filter(first=profil.u,second=adversaire.u,valide=False) and not Duel.objects.filter(first=adversaire.u,second=profil.u,valide=False):
            duel = Duel.objects.create(first=request.user,second=adversaire.u)
            duel.save()
    return redirect ('/')
