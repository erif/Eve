from os.path import join
from django.conf.urls import patterns, include, url
#from .settings import PROJECT_PATH
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Eve.views.home', name='home'),
    # url(r'^Eve/', include('Eve.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^links/', include('Links.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^static/(?P<path>.*)$',
#        'django.views.static.serve',
#        {'document_root': join(PROJECT_PATH, 'static')}),
    
    
)
#urlpatterns += staticfiles_urlpatterns()
