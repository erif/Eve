from django.conf.urls.defaults import patterns, include, url
from .views import Index, About


urlpatterns = patterns('',
    url(r'^$', Index.as_view(),
        name='index'),
    url('^about_us/$', About.as_view(), 
        name='about_eve'),
    
    
    
)