# Create your views here.
# -*- encoding:utf-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.mail import send_mail
from random import randint
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from notification.models import Notification, Titre, Message, Dest
from profil.models import Profil, Localite, VilleProche, Pays, Contact
    
def base(request) :
    if request.method == "POST" :
        if not request.POST['username'] or not request.POST['password'] :
            return redirect(request.POST['url'])
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
            
        if user :
            login(request, user)
        else :
            return render_to_response('profil/inscription.html',{'msg_error':"Utilisateur ou mot de passe inconnu"},RequestContext(request))     
        return redirect(request.POST['url'])
    if request.user.is_active :
        return redirect('/profil/editer/')
    else :
        return render_to_response('profil/inscription.html',{'msg_error':str()},RequestContext(request))     
             
from recaptcha.client import captcha

def nouveau(request) :
    if request.method == "POST" :
        response = captcha.submit(
            request.POST.get('recaptcha_challenge_field'),
            request.POST.get('recaptcha_response_field'),
            '6LfDrPESAAAAABINT7Y69VTIviZLqijba7V3tgeK',
            request.META['REMOTE_ADDR'],
        )
        if not response.is_valid:
            return render_to_response('profil/inscription.html',{'msg_error':response.error_code},RequestContext(request))     
            return redirect('/profil/')
        pseudo = request.POST['pseudo']
        if User.objects.filter(username=pseudo) or Profil.objects.filter(pseudo=pseudo):
            msg = "Ce pseudo est déjà utilisé"
            return render_to_response('profil/inscription.html',{'msg_error':msg},RequestContext(request))     
        elif request.POST['pwd1'] != request.POST['pwd2'] :
            msg = "Mots de passe non identiques"
            return render_to_response('profil/inscription.html',{'msg_error':msg},RequestContext(request))     
        elif " " in request.POST['pseudo'] :
            msg = "Pas d'espace dans un pseudo"
            return render_to_response('profil/inscription.html',{'msg_error':msg},RequestContext(request))     
        else :  
            new_user = User.objects.create(username=pseudo,is_active=True)
            new_user.set_password(request.POST['pwd1'])
            new_user.save()
            new_profil = Profil.objects.create(pseudo=pseudo,u=new_user)
            new_profil.save()
            welcome_msg_titre = Titre.objects.create(titre="Bienvenue sur Hearthstone Romandie")
            welcome_msg_titre.save() 
            welcome_msg_dest = Dest.objects.create(titre=welcome_msg_titre,dest=new_user)
            welcome_msg_dest.save()
            welcome_msg_orig = Dest.objects.create(titre=welcome_msg_titre,dest=User.objects.get(id=44))
            welcome_msg_orig.save()
            msg = """Bienvenue sur Hearthstone Romandie !

N'hésite pas à te [url=http://hearthstone-romandie.ch/forum/topic/add?forum=13]présenter[/url] sur le forum !

Tu peux remplir tes informations personnelles [url=http://hearthstone-romandie.ch/profil/editer/]ici[/url], en précisant à qui tu veux partager ces informations. La localité et la ville proche permettent de mieux rechercher les membres par région, n'hésite pas à compléter ces informations.

Tu peux remplir tes contacts grâce à notre outil [url=http://hearthstone-romandie.ch/profil/recherche/]Membres[/url], expliqué en détail [url=http://hearthstone-romandie.ch/forum/topic/14]ici[/url].

Nous espérons que tu feras des rencontres sympathiques sur ce site, et nous te souhaitons de plaisants duels.

A bientôt !

L'équipe de Hearthstone Romandie"""
            welcome_msg = Message.objects.create(titre=welcome_msg_titre,content=msg,user=User.objects.get(id=44))
            welcome_msg.save()
            admin_msg_titre = Titre.objects.create(titre="Nouveau membre : %s"%new_profil.pseudo)
            admin_msg_titre.save()
            admin_msg_dest = Dest.objects.create(titre=admin_msg_titre,dest=User.objects.get(id=9))
            admin_msg_dest.save()
            admin_msg_orig = Dest.objects.create(titre=admin_msg_titre,dest=User.objects.get(id=44))
            admin_msg_orig.save()
            msg = """Nouveau membre : [url=http://hearthstone-romandie.ch/profil/detail/%d/]%s[/url]"""%(new_profil.id,new_profil.pseudo)
            admin_msg = Message.objects.create(titre=admin_msg_titre,content=msg,user=User.objects.get(id=44))
            admin_msg.save()
            u = authenticate(username=new_user.username,password=request.POST['pwd1'])
            login(request,u)
            return redirect('/profil/')
    else: 
        return redirect('/profil/')

#def validation(request, code, msg=str()) :
#    if User.objects.filter(username=code):
#        return render_to_response('profil/validation.html',{'code':code,'msg_error':msg},RequestContext(request))
#    else :
#        return redirect('/profil/')
        
#def terminate(request) :
#    if request.method == "POST" :
#        if User.objects.filter(username=request.POST['username']) or Profil.objects.filter(pseudo=request.POST['username']) :
#            return render_to_response('profil/validation.html',{'code':request.POST['code'],'msg_error':"Nom de profil déjà utilisé"},RequestContext(request))
#        if request.POST['pwd1'] != request.POST['pwd2'] :
#            return render_to_response('profil/validation.html',{'code':request.POST['code'],'msg_error':"Mots de passe non identiques"},RequestContext(request))
#        try :
#            user = User.objects.get(username=request.POST['code'])
#        except :
#            return redirect('/profil/')
#        profil = Profil.objects.get(u=user)
#        user.username = request.POST['username']
#        profil.pseudo = request.POST['username']
#        user.set_password(request.POST['pwd1'])
#        user.is_active = True
#        user.save()
#        profil.save()
#        u = authenticate(username=user.username,password=request.POST['pwd1'])
#        login(request,u)
#        return redirect('/profil/')
#    else :
#        return redirect('/profil/')

def deco(request) :
    if request.user.is_active :
        logout(request)
    return redirect(request.GET['url'])

def editer(request) :
    msg = list()
    msg_error = list()
    if not request.user.is_active :
        return redirect('/')
    profil = get_object_or_404(Profil,u__id=request.user.id)
    user = get_object_or_404(User,id=request.user.id)
    if request.method == "POST":
        if request.POST['type'] == "edit_profil" :
            if not request.POST['email'] :
                msg_error.append("E-mail obligatoire")
            if Profil.objects.filter(email=request.POST['email']).exclude(u=request.user) or User.objects.filter(email=request.POST['email']).exclude(id=request.user.id) :
                msg_error.append("E-mail déjà utilisé")
            if request.POST['battletag'] and Profil.objects.filter(battletag=request.POST['battletag']).exclude(u=request.user) :
                msg_error.append("BattleTag déjà utilisé")
            if not msg_error :
                profil.avatar = request.POST['avatar']
                profil.nom = request.POST['nom']
                profil.nom_privacy = int(request.POST['nom_privacy'])
                profil.prenom = request.POST['prenom']
                profil.prenom_privacy = int(request.POST['prenom_privacy'])
                profil.email = request.POST['email']
                user.email = request.POST['email']
                profil.email_privacy = int(request.POST['email_privacy'])
                profil.rue = request.POST['rue']
                profil.rue_privacy = int(request.POST['rue_privacy'])
                if request.POST['localite_new'] :
                    if not Localite.objects.filter(localite=request.POST['localite_new']) :
                        localite = Localite.objects.create(localite=request.POST['localite_new'])
                        localite.save()
                    else :
                        localite = Localite.objects.get(localite=request.POST['localite_new'])
                else :
                    localite = Localite.objects.get(id=int(request.POST['localite']))
                profil.localite = localite
    #            profil.localite_privacy = int(request.POST['localite_privacy'])
                if request.POST['ville_proche_new'] :
                    if not VilleProche.objects.filter(ville_proche=request.POST['ville_proche_new']) :
                        ville_proche = VilleProche.objects.create(ville_proche=request.POST['ville_proche_new'])
                        ville_proche.save()
                    else :
                        ville_proche = VilleProche.objects.get(ville_proche=request.POST['ville_proche_new'])
                else :
                    ville_proche = VilleProche.objects.get(id=int(request.POST['ville_proche']))
                profil.ville_proche = ville_proche
    #            profil.ville_proche_privacy = int(request.POST['ville_proche_privacy'])
                if request.POST['pays_new'] :
                    if not Pays.objects.filter(pays=request.POST['pays_new']) :
                        pays = Pays.objects.create(pays=request.POST['pays_new'])
                        pays.save()
                    else :
                        pays = Pays.objects.get(pays=request.POST['pays_new'])
                else :
                    pays = Pays.objects.get(id=int(request.POST['pays']))
                profil.pays = pays
    #            profil.pays_privacy = int(request.POST['pays_privacy'])
                profil.battletag = request.POST['battletag']
                profil.battletag_privacy = int(request.POST['battletag_privacy'])
                profil.telephone = request.POST['telephone']
                profil.telephone_privacy = int(request.POST['telephone_privacy'])
                profil.save()
                user.save()
                msg.append('Votre profil a été modifié')
        if request.POST['type'] == "delete_contact" :
            del_contact = Contact.objects.get(owner=profil,contact=Profil.objects.get(id=int(request.POST['contact'])))
            del_contact.delete()
            msg.append("Contact supprimé")
    contacts = Contact.objects.filter(owner=profil) 

    return render_to_response('profil/modification.html',{'profil':profil,'localite':Localite.objects.all().order_by('localite'),'ville_proche':VilleProche.objects.all().order_by('ville_proche'), 'pays':Pays.objects.all().order_by('pays'), 'contacts':contacts, 'msg':msg,'msg_error':msg_error},RequestContext(request))     

def recherche(request) :
    if request.method == "POST" :
        if request.POST['method'] == "localisation" :
            pays = int(request.POST['pays'])
            ville_proche = int(request.POST['ville_proche'])
            localite = int(request.POST['localite'])
            if pays == 1 and ville_proche == 1 and localite == 1 :
                return redirect('/profil/recherche/')
            temp = Profil.objects.filter(u__is_active=True)
            if pays != 1 :
                temp = temp.filter(pays__id=pays)
            if ville_proche != 1 :
                temp = temp.filter(ville_proche__id=ville_proche)
            if localite != 1 :
                temp = temp.filter(localite__id=localite)
            result = temp.order_by('pseudo')
        elif request.POST['method'] == "pseudo" :
            result = list()
            for prof in Profil.objects.filter(u__is_active=True) :
                if request.POST['pseudo'].lower() in prof.pseudo.lower() :
                    result.append(prof)
        elif request.user.is_active :
            result = list()
            for contact in Contact.objects.filter(owner=Profil.objects.get(u__id=request.user.id)).order_by('contact__pseudo') :
                result.append(Profil.objects.get(id=contact.contact.id))
        else :
            result = list()
    else :
        result = list()
    return render_to_response('profil/recherche.html',{'pays':Pays.objects.all().order_by('pays'),'ville_proche':VilleProche.objects.all().order_by('ville_proche'),'localite':Localite.objects.all().order_by('localite'),'result':result},RequestContext(request))

def details(request,detail_id) :
    msg = str()
    msg_error = str()
    if not Profil.objects.filter(id=detail_id) :
        return redirect('/profil/recherche/')
    contact = False
    for d_c in Contact.objects.filter(owner__id=detail_id) :
        if d_c.contact.u.id == request.user.id :
            contact = True
            break
    owner = Profil.objects.filter(u__id=request.user.id)
    detail = Profil.objects.get(id=detail_id)
    contact_exist = False
    if request.user.is_active :
        contact_exist = Contact.objects.filter(owner__u=request.user).filter(contact=detail)
        if detail.u == request.user :
            contact_exist = 1
            contact = True
    if request.method == "POST" :
        if request.user.is_active :
            if not contact_exist :
                new_contact = Contact.objects.create(owner=owner[0],contact=detail)
                new_contact.save()
                contact_exist = new_contact
                notif = Notification.objects.create(destinataire=detail,contact=new_contact)
                if Contact.objects.filter(owner=detail,contact=owner[0]) :
                    notif.contact_already = True
                notif.save()
                old_contact = Contact.objects.filter(owner=detail,contact=owner[0])
                if old_contact :
                    notif_origin = Notification.objects.filter(destinataire=owner[0]).filter(contact=old_contact[0])
                    if notif_origin :
                        delete_notif = notif_origin[0]
                        delete_notif.vue = True
                        delete_notif.save()
            else :
                msg_error = "Cette personne est déjà dans vos contacts"
        else :
            msg_error = "Vous devez être connecté pour ajouter un contact"
    info = list()
    info.append(detail.pseudo)
    info.append(detail.avatar)
    if detail.nom_privacy == 2 or (detail.nom_privacy == 1 and contact) :
        info.append(detail.nom)
    else :
        info.append("Info non disponible")
    if detail.prenom_privacy == 2 or (detail.prenom_privacy == 1 and contact) :
        info.append(detail.prenom)
    else :
        info.append("Info non disponible")
    if detail.email_privacy == 2 or (detail.email_privacy == 1 and contact) :
        info.append(detail.email)
    else :
        info.append("Info non disponible")
    if detail.rue_privacy == 2 or (detail.rue_privacy == 1 and contact) :
        info.append(detail.rue)
    else :
        info.append("Info non disponible")
    if detail.localite_privacy == 2 or (detail.localite_privacy == 1 and contact) :
        info.append(detail.localite.localite)
    else :
        info.append("Info non disponible")
    if detail.ville_proche_privacy == 2 or (detail.ville_proche_privacy == 1 and contact) :
        info.append(detail.ville_proche.ville_proche)
    else :
        info.append("Info non disponible")
    if detail.pays_privacy == 2 or (detail.pays_privacy == 1 and contact) :
        info.append(detail.pays.pays)
    else :
        info.append("Info non disponible")
    if detail.battletag_privacy == 2 or (detail.battletag_privacy == 1 and contact) :
        info.append(detail.battletag)
    else :
        info.append("Info non disponible")
    if detail.telephone_privacy == 2 or (detail.telephone_privacy == 1 and contact) :
        info.append(detail.telephone)
    else :
        info.append("Info non disponible")
    return render_to_response('profil/detail.html',{'info':info,'contact':contact_exist,'msg':msg,'msg_error':msg_error},RequestContext(request))
     
#TODO change mdp & email, mdp oublié, supprimer profil+user+contacts, messages
