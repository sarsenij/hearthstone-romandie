from django.conf.urls import patterns, url

from profil import views
urlpatterns = patterns('',
    # Example:
    # (r'^test_project/', include('test_project.foo.urls')),
    url(r'^nouveau/$', views.nouveau),
#    url(r'^validation/(?P<code>\d{16})/$', views.validation),
#    url(r'^terminate/$', views.terminate),
    url(r'^deco/$', views.deco),
    url(r'^send_email$', views.send_email),
    url(r'^send_email/$', views.send_email),
    url(r'^check_email$', views.check_email),
    url(r'^settings$', views.settings),
    url(r'^settings/$', views.settings),
    url(r'^changepwd/$', views.changepwd),
    url(r'^resetpwd/$', views.resetpwd),
    url(r'^recherche/$', views.recherche),
    url(r'^detail/(?P<detail_id>\d+)/$', views.details),
    url(r'^$', views.base),
)
