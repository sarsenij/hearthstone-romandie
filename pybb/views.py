# -*- coding: utf-8 -*-
import logging

from django.shortcuts import redirect, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponse

from django.contrib.auth.models import User

from common.pagination import paginate
from datetime import datetime

from pybb.models import Category, Forum, Topic, Post, Dejavu, Suivi
from pybb.forms import PostForm, TopicForm, TopicDeleteForm
from profil.models import Profil


def get_post_form(request, topic):
    if request.user.is_authenticated():
        instance = Post(topic=topic, user=request.user)
        form = PostForm(request.POST or None, instance=instance)
        return form
    else:
        return None

def home_page(request):
    if request.user.is_staff :
        cats = Category.objects.order_by('position')
    else :
        cats = Category.objects.all().exclude(staff=True).order_by('position')
    dejavu = dict()
    if request.user.is_staff :
        forums = Forum.objects.all()
    else :
        forums = Forum.objects.all().exclude(staff=True)
    for forum in forums :
        dejavu[forum] = 1 #Pas d'indicateur pour les non membres
        if request.user.is_active :
            dejavu[forum] = 0 # Nouveau(x) topic(s)
            dv = Dejavu.objects.filter(compte=request.user).filter(forum=forum)
            if len(dv) == len(Topic.objects.filter(forum=forum)):
                dejavu[forum] = 1 #Tout vu
            for d in dv :
                if d.post != Post.objects.filter(topic=d.topic).order_by('-created')[0].id and dejavu[forum] :
                    dejavu[forum] = 2 #Nouveau post
                    break
    if request.user.is_active :
        suivis = Suivi.objects.filter(user=request.user)
    else :
        suivis = list()
    dvsuivi = dict()
    for topic in suivis :
        dvsuivi[topic] = [1,0,0] #Pas d'indicateur pour les non membres
        if request.user.is_active :
            dv = Dejavu.objects.filter(compte=request.user).filter(topic=topic.topic)
            if not dv :
                dvsuivi[topic] = [0,0,0] #Pas visité
            else :
                if dv[0].post :
                    post_page = list(Post.objects.filter(topic=topic.topic).order_by('created').values_list('id',flat=True)).index(dv[0].post)/10
                else :
                    post_page = 0
                if dv[0].post == Post.objects.filter(topic=topic.topic).order_by('-created')[0].id:
                    dvsuivi[topic] = [1,post_page,dv[0].post] #Tout vu
                else :
                    dvsuivi[topic] = [2,post_page,dv[0].post] #Nouveau post
            
    context = {'cats': cats,
            'dejavu': dejavu,
            'suivis': suivis,
            'dvsuivi': dvsuivi,
            }
    return render(request, 'pybb/home_page.html', context)


def forum_page(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    if forum.staff and not request.user.is_staff :
        return redirect('/forum/')
    dejavu = dict()
    postit = Topic.objects.filter(forum=forum,postit=True)
    normal = Topic.objects.filter(forum=forum,postit=False)
    for topics in [postit, normal] :
        for topic in topics :
            dejavu[topic] = [1,0,0] #Pas d'indicateur pour les non membres
            if request.user.is_active :
                dv = Dejavu.objects.filter(compte=request.user).filter(topic=topic)
                if not dv :
                    dejavu[topic] = [0,0,0] #Pas visité
                else :
                    posts = Post.objects.filter(topic=topic).order_by('created')
                    if dv[0].post in list(posts.values_list('id',flat=True)):
                        post_page = list(Post.objects.filter(topic=topic).order_by('created').values_list('id',flat=True)).index(dv[0].post)/10
                    else :
                        post_page = 0
                    if dv[0].post == posts.order_by('-created')[0].id:
                        dejavu[topic] = [1,post_page,dv[0].post] #Tout vu
                    else :
                        dejavu[topic] = [2,post_page,dv[0].post] #Nouveau post
                
    context = {'forums':[postit,normal],
            'forum':forum,
            'dejavu': dejavu,
            }
    return render(request, 'pybb/forum_page.html', context)


def topic_page(request, pk, page=0):
    page = int(page)
    first_post = int(page)*10
    topic = get_object_or_404(Topic, pk=pk)
    if topic.staff and not request.user.is_staff :
        return redirect('/forum/')
    posts = Post.objects.filter(topic=topic).order_by('created')
    #pages = len(posts)/10
    #if len(posts)%10 :
    #    pages += 1
    #if page > pages-1 :
    #    raise Http404
    pages = len(posts)/10
    if len(posts)%10 :
        pages += 1
    if page+1 > pages :
        raise Http404
    #try :
    if len(posts) <= (first_post+10) :
        posts = posts[first_post:]
    else :
        posts = posts[first_post:first_post+10]
    #except :
    post_form = get_post_form(request, topic)
    if request.user.is_active :
        suivi = Suivi.objects.filter(topic=topic,user=request.user)
    else :
        suivi = list()
    context = {'topic': topic,
               'posts': posts,
               'pages': range(pages),
               'post_form': post_form,
               'page': page,
               'suivi': suivi, 
               'forums':Forum.objects.all()
            }
    if request.user.is_active and posts:
        if Dejavu.objects.filter(compte=request.user).filter(topic=topic):
            dejavu = Dejavu.objects.get(compte=request.user,topic=topic)
            dejavu_post = dejavu.post
        else: 
            dejavu = Dejavu.objects.create(compte=request.user,topic=topic,forum=topic.forum)
            dejavu_post = 0
        if dejavu_post < posts[-1].id :
            dejavu.post = posts[-1].id
            dejavu.save()
    return render(request, 'pybb/topic_page.html', context)


@login_required
def post_add(request):
    topic_id = request.GET.get('topic')
    topic = get_object_or_404(Topic, pk=topic_id)
    form = get_post_form(request, topic)
    if not topic.close and form.is_valid():
        topic.edit=datetime.now()
        topic.save()
        form.save()
        if not Suivi.objects.filter(topic=topic,user=User.objects.get(id=9)) :
            suivi = Suivi.objects.create(user=User.objects.get(id=9),topic=topic)
            suivi.save()
        posts = Post.objects.filter(topic=topic).order_by('-created')
        page = (len(posts)-1)/10
        post = posts[0].id
        return redirect('/forum/topic/%s/%s#Post%d'%(topic_id,page,post))
    context = {'form': form,
               'topic': topic,
            }
    return render(request, 'pybb/post_add.html', context)

@login_required
def post_modify(request,post):
    topic_id = request.GET.get('topic')
    topic = get_object_or_404(Topic, pk=topic_id)
    post = get_object_or_404(Post, id=int(post))
    posts = Post.objects.filter(topic=topic).order_by('created')
    page = list(posts.values_list('id', flat=True)).index(post.id)/10
    if (request.user == post.user and not post.locked and not topic.close) or request.user.is_staff :
        if posts[0] == post :
            first_post = True
        else :
            first_post = False
        if request.method == "POST" :
            post.content = request.POST['content']
            post.modif_user = request.user
            post.modif_date = datetime.now()
            post.deleted = False
            post.save()
            if first_post :
                topic.name = request.POST['topic_name']
                topic.save()
            return redirect('%s/%s#Post%s'%(topic.get_absolute_url(),str(page),str(post.id)))
        context = {'post':post,'topic':topic,'first_post':first_post,}
        return render(request, 'pybb/post_modify.html', context)
    else :
        return redirect('%s/%s#Post%s'%(topic.get_absolute_url(),str(page),str(post.id)))

@login_required
def post_delete(request,post):
    topic_id = request.GET.get('topic')
    topic = get_object_or_404(Topic, pk=topic_id)
    post = get_object_or_404(Post, id=int(post))
    if request.user == post.user or request.user.is_staff :
        if request.user.is_staff and request.user != post.user :
            post.locked = True
        post.deleted = True
        post.deleted_by = request.user
        post.save()
        page = list(Post.objects.filter(topic=topic).order_by('created').values_list('id', flat=True)).index(post.id)/10
    return redirect('%s/%s#Post%s'%(topic.get_absolute_url(),str(page),str(post.id)))

@login_required
def topic_add(request):
    forum_id = request.GET.get('forum')
    forum = get_object_or_404(Forum, pk=forum_id)
    form = TopicForm(request.POST or None)
    if form.is_valid():
        topic = Topic.objects.create(
            name=form.cleaned_data['name'],
            forum=forum)
        post = Post.objects.create(
            topic=topic,
            user=request.user,
            content=form.cleaned_data['content'],
        )
        suivi = Suivi.objects.create(user=User.objects.get(id=9),topic=topic)
        dv = Dejavu.objects.create(compte=User.objects.get(id=9),forum=forum,topic=topic,post=0)
        messages.success(request, u'Topic ajouté')
        return redirect(topic)
    context = {'form': form,
               'forum': forum,
            }
    return render(request, 'pybb/topic_add.html', context)

@login_required
def topic_postit(request,topic):
    if request.user.is_staff :
        forum_id = request.GET.get('forum')
        forum = get_object_or_404(Forum, pk=forum_id)
        topic = get_object_or_404(Topic, pk=topic)
        if topic.postit :
            topic.postit = False
        else :
            topic.postit = True
        topic.save()
    return redirect(forum.get_absolute_url())


@login_required
def topic_close(request,topic):
    if request.user.is_staff :
        forum_id = request.GET.get('forum')
        forum = get_object_or_404(Forum, pk=forum_id)
        topic = get_object_or_404(Topic, pk=topic)
        if topic.close :
            topic.close = False
        else :
            topic.close = True
        topic.save()
    return redirect(forum.get_absolute_url())

@login_required
def topic_delete(request,topic):
    if request.user.is_staff :
        forum_id = request.GET.get('forum')
        forum = get_object_or_404(Forum, pk=forum_id)
        topic = get_object_or_404(Topic, pk=topic)
        posts = Post.objects.filter(topic=topic)
        forum.topic_count -= 1
        forum.post_count -= len(posts)
        forum.save()
        del_forum = Forum.objects.get(id=19)
        del_forum.topic_count += 1
        del_forum.post_count += len(posts)
        del_forum.save()
        topic.staff = True
        topic.forum = del_forum
        topic.name = "(%s) %s"%(forum.name,topic.name)
        topic.close = True
        topic.save()
        for dv in Dejavu.objects.filter(topic=topic) :
            dv.forum = del_forum
            dv.save()
    return redirect(forum.get_absolute_url())

def suivi(request):
    if request.method == "POST" and request.user.is_active :
        topic = get_object_or_404(Topic, pk=request.POST['topic'])
        try :
            request.POST['add']
            add = True
        except :
            add = False
            
        if add and not Suivi.objects.filter(topic=topic,user=request.user) :
            suivi = Suivi.objects.create(user=request.user,topic=topic)
            suivi.save()
        elif not add and Suivi.objects.filter(topic=topic,user=request.user) :
            suivi = Suivi.objects.get(topic=topic,user=request.user)
            suivi.delete()
    return HttpResponse()

def topic_move(request,topic):
    topic = get_object_or_404(Topic, pk=topic)
    if request.user.is_staff and request.GET.get('destination') != "":
        forum_id = request.GET.get('forum')
        forum = get_object_or_404(Forum, pk=forum_id)
        destination_id = request.GET.get('destination')
        destination = get_object_or_404(Forum, pk=destination_id)
        posts = Post.objects.filter(topic=topic)
        forum.topic_count -= 1
        forum.post_count -= len(posts)
        forum.save()
        destination.topic_count += 1
        destination.post_count += len(posts)
        destination.save()
        if destination_id == '1' :
            topic.created = datetime.now()
        topic.forum = destination
        topic.save()
        for dv in Dejavu.objects.filter(topic=topic) :
            dv.forum = destination
            dv.save()
        return redirect(destination.get_absolute_url())
    return redirect(topic.get_absolute_url())
