from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required as auth
from .views import Index, About, LinkAdd, LinkList, TagView, LinkDelete, UserProfileDetailView, UserProfileEditView, MyLinks
from .models import Link, UserProfile


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
    url('^tags/$', TagView.as_view(),
        name='tagView'),
    url('^delete/(?P<pk>\d+)/$', LinkDelete.as_view(model=Link, template_name='Link/link_confirm_delete.html'),
        name='deleteLink'),
    
    url('^mylinks/$', MyLinks.as_view(),
        name='mylinks'),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(),
        name="profile"),
    url(r'edit_profile/$', auth(UserProfileEditView.as_view()),
        name="edit_profile"),

     
)