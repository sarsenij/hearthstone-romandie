from django.conf.urls import patterns, url

from profil import views
urlpatterns = patterns('',
    # Example:
    # (r'^test_project/', include('test_project.foo.urls')),
    url(r'^editer/$', views.editer),
    url(r'^nouveau/$', views.nouveau),
#    url(r'^validation/(?P<code>\d{16})/$', views.validation),
#    url(r'^terminate/$', views.terminate),
    url(r'^deco/$', views.deco),
    url(r'^recherche/$', views.recherche),
    url(r'^detail/(?P<detail_id>\d+)/$', views.details),
    url(r'^$', views.base),
)
