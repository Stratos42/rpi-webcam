from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', include('camera.urls')),
                       url(r'^cameras/', include('camera.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
