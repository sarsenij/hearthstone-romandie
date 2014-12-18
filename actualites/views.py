# Create your views here.
# -*- encoding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from pybb.models import Post, Topic
from notification.models import Notification
from profil.models import Contact, Profil

def actualites(request) :
    if request.method == "POST" :
        try :
            request.POST['vu']
            vu = True
        except :
            vu = False
        if vu :
            notif = Notification.objects.filter(id=int(request.POST['vu']))
            if notif :
                save_notif = notif[0]
                save_notif.vue = True
                save_notif.save()
        try : 
            request.POST['add']
            add = True
        except :
            add = False
        if add :
            new_contact = Contact.objects.create(owner=Profil.objects.get(u__id=request.user.id),contact=Profil.objects.get(id=int(request.POST['add'])))
            new_contact.save()
            notif = Notification.objects.get(id=int(request.POST['id']))
            notif.vue = True
            notif.save()
            notif2 = Notification.objects.create(destinataire=new_contact.contact,contact=new_contact,contact_already=True)
            notif2.save()
            
    acts = list()
    topics = list()
    for p in Topic.objects.filter(forum__id=1).order_by('-created') :
        if len(acts) >= 10 :
            break
        if not p in topics :
            for po in Post.objects.filter(topic__forum__id=1).order_by('id') :
                if po.topic == p :
                    acts.append(po)
                    break
            topics.append(p)
    return render_to_response('actualites/actualites.html',{'acts':acts},RequestContext(request))

def stream(request):
    return render_to_response('stream/stream.html',{},RequestContext(request))
