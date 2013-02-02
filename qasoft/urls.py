from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import ajax

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^ajax/', include('ajax.urls')),
    url(r'^question/list$', 'forum.views.list_question', name='home'),
    url(r'^question/submit$', 'forum.views.submit_question', name='home'),
    url(r'^question/view/(?P<slug>[-\w]+)/$','forum.views.view_question',),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
