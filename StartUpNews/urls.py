from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.static import static


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$','StartUpNews.views.home'),
    url(r'^accounts/register/$','StartUpNews.views.register_user'),
    url(r'^accounts/register_success/$','StartUpNews.views.register_success'),

    url(r'^accounts/login/$','StartUpNews.views.login'),
    url(r'^accounts/auth/$','StartUpNews.views.auth_view'),
    url(r'^accounts/logout/$','StartUpNews.views.logout'),
    url(r'^accounts/loggedin/$','StartUpNews.views.loggedin'),
    url(r'^accounts/invalid/$','StartUpNews.views.invalid_login'),


    # Examples:
    #url(r'^$', 'News.views.index', name='home'),
    #url(r'full_news', 'News.views.full_news', name='full_news'),
    #url(r'^StartUpNews/', include('StartUpNews.foo.urls')),
    url(r'^svnews/$', 'News.views.index'),
    #url(r'^(?P<pk>\d+)$', include('News.urls')),
    url(r'^svnews/(?P<pk>\d+)$', 'News.views.full_news',name='full_news'),
    
    (r'^static/', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
