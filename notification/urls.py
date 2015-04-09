from django.conf.urls import patterns, url

from notification import views
urlpatterns = patterns('',
    # Example:
    # (r'^test_project/', include('test_project.foo.urls')),
#    url(r'^$', views.base),
    url(r'^indicator/$', views.notif),
    url(r'^messages/$', views.messages),
    url(r'^notification/$', views.notification),
    url(r'^message/(?P<titre>\d+)/$', views.message_detail),
    url(r'^new_message/$', views.new_message),
#    url(r'^message/$', views.message),
)
