# Create your views here.
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from datetime import datetime

from notification.models import Notification, Titre, Message, Dest, Dejavu, ChatMsg
from pybb.models import Suivi, Dejavu as PostDv, Post, Topic
from profil.models import Profil, Contact

def notif(request):
    if request.user.is_active :
        if request.method == "POST" :
            if request.POST['message'] :
                ch = ChatMsg.objects.create(user=request.user,message=request.POST['message'])
                ch.save()

    return render_to_response('notification/indicateur.html',{},RequestContext(request))

def messages(request):
    if not request.user.is_active :
        return redirect('/')
    non_lu = list()
    lu = list()
    for titre in Dest.objects.filter(dest=request.user).order_by('-titre__edit'):
        dejavu = Dejavu.objects.filter(titre=titre.titre,compte=request.user)
        last_message = Message.objects.filter(titre=titre.titre).order_by('-created')[0]
        if not dejavu or dejavu[0].message != last_message :
            non_lu.append(titre.titre)
        else :
            lu.append(titre.titre)
    return render_to_response('notification/messages.html',{'lu':lu,'non_lu':non_lu,'dest':Dest.objects.all()},RequestContext(request))

def message_detail(request,titre):
    if not request.user.is_active :
        return redirect('/')
    ok = False
    for d in Dest.objects.filter(titre=Titre.objects.get(pk=titre)) :
        if d.dest == request.user :
            ok = True
    if not ok :
        return redirect('/')
    titre = int(titre)
    msg_titre = get_object_or_404(Titre, id=titre)
    if request.method == "POST" and request.POST['content'].replace(" ","") != "" :
        msg = Message.objects.create(content=request.POST['content'],user=request.user,titre=msg_titre)
        msg_titre.edit = datetime.now()
        msg_titre.save()
        msg.save()
    all_messages = Message.objects.filter(titre=msg_titre).order_by('-created')
    dv = Dejavu.objects.filter(titre=msg_titre,compte=request.user)
    if dv :
        dv = dv[0]
        dv.message = all_messages[0]
    else :
        dv = Dejavu.objects.create(compte=request.user,titre=msg_titre,message=all_messages[0]) 
    dv.save()
    return render_to_response('notification/message_detail.html',{'all_messages':all_messages.order_by('created')},RequestContext(request))

def new_message(request):
    if request.method == "POST" and request.user.is_active:
        if request.POST['content'].replace(" ","") == "" :
            return redirect('/notification/new_message/')
        if request.POST['titre'].replace(" ","") == "" :
            titre = "(pas de sujet)"
        else :
            titre = request.POST['titre']
        destinataires = request.POST['destinataires'].split(' ')
        msg_titre = Titre.objects.create(titre=titre)
        msg_titre.save()
        msg = Message.objects.create(titre=msg_titre,user=request.user,content=request.POST['content'])
        msg.save()
        incr = 0
        for dest in destinataires :
            if dest :
                incr += 1
                try :
                    d = Profil.objects.get(pseudo=dest)
                    if not Dest.objects.filter(titre=msg_titre,dest=d.u) :
                        d_create = Dest.objects.create(titre=msg_titre,dest=d.u)
                        d_create.save()
                except :
                    pass
        if not incr :
            return redirect('/notification/new_message/')
        else :
            if not Dest.objects.filter(titre=msg_titre,dest=request.user) :
                d_create = Dest.objects.create(titre=msg_titre,dest=request.user)
                d_create.save()
        url = "/notification/message/"+str(msg_titre.id)+"/"
        return redirect(url)
    else :
        if request.user.is_active :
            contacts = Contact.objects.filter(owner=Profil.objects.get(u=request.user)).order_by('contact__pseudo')
        else :
            contacts = list()
        membres = Profil.objects.filter(u__is_active=True).order_by('pseudo')
        if request.GET.get('dest'):
            dest = request.GET.get('dest')
        else :
            dest = ""
        return render_to_response('notification/new_message.html',{'contacts':contacts,'membres':membres,'dest':dest},RequestContext(request))
