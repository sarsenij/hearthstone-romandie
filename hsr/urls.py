from django.conf.urls import patterns, include
from django.contrib import admin

from actualites import views as actualites

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^test_project/', include('test_project.foo.urls')),

    ('^admin/', include(admin.site.urls)),

    ('^profil/', include('profil.urls')),
    ('^notification/', include('notification.urls')),
    ('^forum/', include('pybb.urls', namespace='pybb')),
    (r'^$', actualites.actualites),
)
