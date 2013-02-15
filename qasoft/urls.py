from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import ajax
import forum

from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^ajax/', include('ajax.urls')),
    url(r'^question/', include('forum.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simpleinvitation.urls'), ),
)

if not settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
