from profil.models import Profil
from notification.models import Notification, Dest, Dejavu, ChatMsg
from pybb.models import Dejavu as PostDv, Post, Suivi, Topic

def notif(request):
    if request.user.is_active :
        profil = Profil.objects.get(u=request.user)
        contacts = Notification.objects.filter(destinataire=profil,vue=False,contact__isnull=False)
        messages = 0
        for titre in Dest.objects.filter(dest=request.user) :
            dv = Dejavu.objects.filter(titre=titre.titre,compte=request.user)
            if not dv or titre.titre.message_set.all().order_by('-created')[0]!= dv[0].message :
                messages += 1
        chat = ChatMsg.objects.all().order_by('-id')
        if len(chat) > 10 :
            chat = chat[0:10]
        chat = reversed(chat)
        suivistmp = Suivi.objects.filter(user=request.user)
        suivis = list()
        for suivi in suivistmp :
            postdv = PostDv.objects.get(topic=suivi.topic,compte=request.user).post
            if postdv != Post.objects.filter(topic=suivi.topic).order_by('-created')[0].id :
                suivis.append([Topic.objects.get(id=suivi.topic.id),postdv])
    else :
        contacts = list()
        messages = 0
        chat = list()
        suivis = list()
    contenu = {
        'notif_contacts':contacts,
        'notif_messages':messages,
        'notif_chat':chat,
        'notif_suivis':suivis,
    }
    return contenu