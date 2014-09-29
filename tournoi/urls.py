from django.conf.urls import patterns, url

urlpatterns = patterns('tournoi.views',
    # Example:
    # (r'^test_project/', include('test_project.foo.urls')),
    url(r'^$', 'home_page', name='home_page'),
    url(r'^create/$', 'create', name='create'),
    url(r'^detail/(\d+)$', 'detail', name='detail'),
    url(r'^arbre/(\d+)$', 'arbre', name='arbre'),
    url(r'^update/(\d+)$', 'update_score', name='update_score'),
    url(r'^inscription/(\d+)$', 'inscription', name='inscription'),
    url(r'^desinscription/(\d+)$', 'desinscription', name='desinscription'),
)
