from django.conf.urls import patterns, url

from camera import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<camera_room_id>\d+)/$', views.camera_room, name='camera_room'),
)
