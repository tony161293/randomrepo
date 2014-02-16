from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^/svnews/$', 'News.views.index', name='index'),
    #url(r'^(?P<pk>\d+)$', ),
    #url(r'^(?P<pk>\d+)$', 'News.views.full_news', name='full_news'),
#) 

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
