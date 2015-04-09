from datetime import datetime, timedelta
from profil.models import Profil
from notification.models import Notification, Dest, Dejavu, ChatMsg, InviteTournoi, ConvDest, ConvDV
from pybb.models import Dejavu as PostDv, Post, Suivi, Topic

def notif(request):
    if request.user.is_active :
        profil = Profil.objects.get(u=request.user)
        contacts = Notification.objects.filter(destinataire=profil,vue=False,contact__isnull=False)
        messages = 0
        for conv in ConvDest.objects.filter(user=request.user) :
            dv = ConvDV.objects.filter(user=request.user,conv=conv.conv)
            convmsg = conv.conv.convmessage_conv.all().order_by('-date')
            if convmsg and (not dv or convmsg[0] != dv[0].message) :
                messages +=1
        #chat = reversed(chat)
        suivistmp = Suivi.objects.filter(user=request.user)
        suivis = list()
        for suivi in suivistmp :
            postdv = PostDv.objects.get(topic=suivi.topic,compte=request.user).post
            if postdv != Post.objects.filter(topic=suivi.topic).order_by('-created')[0].id :
                suivis.append([Topic.objects.get(id=suivi.topic.id),postdv])
        lastseen = Profil.objects.filter(lastseen__gte=datetime.now()-timedelta(minutes=1)).order_by('pseudo')
        profil = Profil.objects.get(u=request.user)
        profil.lastseen = datetime.now()
        profil.save()
        invtournois = InviteTournoi.objects.filter(user=request.user,staff=False,seen=False)
        stafftournois = InviteTournoi.objects.filter(user=request.user,staff=True,seen=False)
    else :
        contacts = list()
        messages = 0
        suivis = list()
        lastseen = list()
        invtournois = list()
        stafftournois = list()
    chat = ChatMsg.objects.all().order_by('-id')
    if len(chat) > 10 :
        chat = chat[0:10]
    contenu = {
        'notif_contacts':contacts,
        'notif_messages':messages,
        'notif_chat':chat,
        'notif_suivis':suivis,
        'notif_lastseen':lastseen,
        'notif_invtournois':invtournois,
        'notif_stafftournois':stafftournois,
        'notif_nombre':len(contacts)+len(suivis)+len(invtournois)+len(stafftournois),
    }
    return contenu
