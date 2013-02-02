from django.conf.urls import patterns, url

urlpatterns = patterns('forum.views',
    url(r'^list$', 'list_question'),
    url(r'^submit$', 'submit_question'),
    url(r'^view/(?P<slug>[-\w]+)/$','view_question',),
)
