
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('login.urls')),
    url(r'^accounts/', include('requestmanager.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #for get functions
    (r'^accounts/', include('userprofile.urls')),
    
)
