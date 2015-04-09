# Create your views here.
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from datetime import datetime

from notification.models import Notification, Titre, Message, Dest, Dejavu, ChatMsg, Conv, ConvDest, ConvMessage, ConvDV, InviteTournoi
from pybb.models import Suivi, Dejavu as PostDv, Post, Topic
from profil.models import Profil, Contact
from django.contrib.auth.models import User

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
    contacts = Contact.objects.filter(owner=Profil.objects.get(u=request.user)).order_by('contact__pseudo')
    convs = ConvDest.objects.filter(user=request.user).order_by('-conv__last_msg')
    for conv in convs :
        convdv = ConvDV.objects.filter(conv=conv.conv,user=request.user)
        messages = ConvMessage.objects.filter(conv=conv.conv).order_by('date')
        if messages :
            last_message = ConvMessage.objects.filter(conv=conv.conv).order_by('-date')[0]
            if not convdv or convdv[0].message != last_message :
                non_lu.append(conv.conv)
            else :
                lu.append(conv.conv)
    return render_to_response('notification/messages.html',{'lu':lu,'non_lu':non_lu,'contacts':contacts},RequestContext(request))

def message_detail(request,titre):
    if not request.user.is_active :
        return redirect('/')
    if titre == '0' :
        mesconv = list()
        for el in ConvDest.objects.filter(user=request.user) :
            mesconv.append(el.conv)
        conv = False
        for dest in ConvDest.objects.filter(user=User.objects.get(id=int(request.GET.get('dest')))):
            if dest.conv in mesconv :
                conv = dest.conv
                break
        if not conv :
            conv = Conv.objects.create()
            conv.save()
            cd1 = ConvDest.objects.create(user=request.user,conv=conv)
            cd1.save()
            cd2 = ConvDest.objects.create(user=User.objects.get(pk=request.GET.get('dest')),conv=conv)
            cd2.save()
    else :
        conv = get_object_or_404(Conv,pk=titre)
    messages = ConvMessage.objects.filter(conv=conv)
    if ConvDV.objects.filter(user=request.user,conv=conv) :
        convdv = ConvDV.objects.get(user=request.user,conv=conv)
        if messages :
            convdv.message = messages.order_by('-date')[0]
    else :
        convdv = ConvDV.objects.create(user=request.user,conv=conv)
    convdv.save()
    if request.GET.get('refresh') :
        return render_to_response('notification/message_refresh.html',{'messages':messages.order_by('date')},RequestContext(request))
    return render_to_response('notification/message_detail.html',{'messages':messages.order_by('date'),'conv':conv.id,'dest':ConvDest.objects.filter(conv=conv).exclude(user=request.user)},RequestContext(request))

def new_message(request):
    if request.method == "POST" and request.user.is_active:
        if request.POST['message'].replace(" ","") == "" :
            return redirect('/')
        newm = ConvMessage.objects.create(conv=Conv.objects.get(pk=request.POST['conv']),message=request.POST['message'],user=request.user)
        newm.save()
        convdv = ConvDV.objects.get(user=request.user,conv=Conv.objects.get(pk=request.POST['conv']))
        convdv.message = newm
        convdv.save()
        conv = newm.conv
        conv.last_msg = datetime.now()
        conv.save()
    return redirect('/')

def notification(request):
    rarcontacts = Notification.objects.filter(destinataire=Profil.objects.get(u=request.user),contact__isnull=False)
    contacts = rarcontacts.filter(vue=False)
    for contact in contacts :
        contact.vue = True
        contact.save()
    rartournois = InviteTournoi.objects.filter(user=request.user)
    invtournois = rartournois.filter(seen=False,staff=False)
    stafftournois = rartournois.filter(seen=False,staff=True)
    for tournoi in invtournois :
        tournoi.seen = True
        tournoi.save()    
    for tournoi in stafftournois :
        tournoi.seen = True
        tournoi.save()    
    return render_to_response('notification/notification.html',{'rarcontacts':rarcontacts,'rartournois':rartournois,'contacts':contacts,'invtournois':invtournois,'stafftournois':stafftournois},RequestContext(request))
