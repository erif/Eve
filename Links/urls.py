from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView
from .views import Index, About, LinkAdd, LinkList
from .models import Link


urlpatterns = patterns('',
    url(r'^$', Index.as_view(),
        name='index'),
    url('^about/$', About.as_view(), 
        name='about'),
    url('^addLink/$', LinkAdd.as_view(), 
        name='addLink'),
    url('^listLink/$', LinkList.as_view(), 
        name='listLink'),

    url('^detailsLink/(?P<pk>\d+)/$', DetailView.as_view(model=Link, context_object_name='item', 
                                    template_name='Link/link_detail.html'), 
        name='detailsLink'),
    
    
    
    
)