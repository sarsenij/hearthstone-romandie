from datetime import datetime, timedelta
from profil.models import Profil
from notification.models import Notification, Dest, ChatMsg, InviteTournoi, ConvDest, ConvDV
from pybb.models import Dejavu as PostDv, Post, Suivi, Topic, Dejavu
from tournoi.models import Match, Duel

def notif(request):
    if request.user.is_active :
        profil = Profil.objects.get(u=request.user)

        contacts = Notification.objects.filter(destinataire=profil,vue=False,contact__isnull=False)

        messages = len(ConvDV.objects.filter(user=request.user,new=True))

        suivis = list()
        for suivi in Suivi.objects.filter(user=request.user) :
            dv = Dejavu.objects.get(topic=suivi.topic,compte=request.user)
            if dv.new :
                suivis.append([Topic.objects.get(id=suivi.topic.id),PostDv.objects.get(topic=suivi.topic,compte=request.user).post])
        


        lastseen = Profil.objects.filter(lastseen__gte=datetime.now()-timedelta(minutes=1)).order_by('pseudo')

        invtournois = InviteTournoi.objects.filter(user=request.user,staff=False,seen=False)

        stafftournois = InviteTournoi.objects.filter(user=request.user,staff=True,seen=False)

        matchs = list()
        for match in Match.objects.filter(first=request.user,second__isnull=False,valide=False) :
            matchs.append(match)
        for match in Match.objects.filter(first__isnull=False,second=request.user,valide=False) :
            matchs.append(match)
    
        duels = list()
        for match in Duel.objects.filter(first=request.user,second__isnull=False,valide=False) :
            duels.append(match)
        for match in Duel.objects.filter(first__isnull=False,second=request.user,valide=False) :
            duels.append(match)

        news = len(contacts)+len(suivis)+len(invtournois)+len(stafftournois)+messages+len(matchs)+len(duels)
        if profil.sound and news > profil.news :
            sound = True 
        else :
            sound = False
        profil.news = news

        profil.lastseen = datetime.now()

        profil.save()

        if not profil.email_sent :
            profil_step = "send_email"
        elif not profil.email_verified :
            profil_step = "check_email"
        elif not profil.step_settings :
            profil_step = "settings"
        else :
            profil_step = ""

               

    else :
        contacts = list()
        messages = 0
        suivis = list()
        lastseen = list()
        invtournois = list()
        stafftournois = list()
        sound = False
        profil_step = ''
        matchs = list()
        duels = list()
    chat = ChatMsg.objects.all().order_by('-id')
    if len(chat) > 20 :
        chat = chat[0:20]
    contenu = {
        'notif_contacts':contacts,
        'notif_messages':messages,
        'notif_chat':chat,
        'notif_suivis':suivis,
        'notif_lastseen':lastseen,
        'notif_invtournois':invtournois,
        'notif_stafftournois':stafftournois,
        'notif_nombre':len(contacts)+len(suivis)+len(invtournois)+len(stafftournois),
        'notif_sound':sound,
        'notif_profil_step':profil_step,
        'notif_matchs':matchs,
        'notif_duels':duels,
    }
    return contenu
