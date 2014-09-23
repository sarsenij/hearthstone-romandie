# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
urlpatterns = patterns('pybb.views',
    url(r'^$', 'home_page', name='home_page'),
    url(r'^forum/(\d+)$', 'forum_page', name='forum_page'),
    url(r'^topic/(\d+)$', 'topic_page', name='topic_page'),
    url(r'^topic/(\d+)/(\d+)$', 'topic_page', name='topic_page'),
    url(r'^post/add$', 'post_add', name='post_add'),
    url(r'^topic/add$', 'topic_add', name='topic_add'),
    url(r'^topic/postit/(\d+)$', 'topic_postit', name='topic_postit'),
    url(r'^topic/close/(\d+)$', 'topic_close', name='topic_close'),
    url(r'^topic/delete/(\d+)$', 'topic_delete', name='topic_delete'),
    url(r'^post/modify/(\d+)$', 'post_modify', name='post_modify'),
    url(r'^post/delete/(\d+)$', 'post_delete', name='post_delete'),
    url(r'^suivi$', 'suivi', name='suivi'),
    url(r'^topic/move/(\d+)$', 'topic_move', name='topic_move'),
)
