# Create your views here.
import datetime

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from endless_pagination.views import AjaxListView
from django.utils import timezone
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Link, UserProfile
from .forms import LinkForm, DeleteLinkForm, UserProfileForm

from taggit.models import Tag 


class Index(TemplateView):
    template_name = 'Links/index.html'

class About(TemplateView):
    template_name = 'Links/about.html'
    
class LinkAdd(CreateView):
    template_name = 'Links/addLink.html'#cambiar por link_form.html
    model = Link
    form_class = LinkForm
    def post(self, request, *args, **kwargs):
        link_form = LinkForm(request.POST)
        if(link_form.is_valid()):
            saved_link = link_form.save(commit=False)
            saved_link.posted_by = request.user
            saved_link.save()
            return HttpResponseRedirect(reverse('detailsLink', args=(saved_link.id,)))
        else:
            return self.get(request, link_form=LinkForm, *args, **kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LinkAdd, self).dispatch(request, *args, **kwargs)
        

class LinkList(ListView):
    template_name = 'Links/listLink.html'
    model = Link
    paginate_by = 10
    
    def get_queryset(self):
        return Link.objects.order_by('-date_posted') 
    
    def set_context_page_slice(self, context, delta=10):
        min_slice = context['page_obj'].number - delta
        max_slice = context['page_obj'].number + delta
        min_slice = 0 if min_slice < 0 else min_slice
        context['min_page_slice'] = min_slice
        context['max_page_slice'] = max_slice
        context['page_slice'] = '%s:%s' % (min_slice, max_slice)
    
    def get_context_data(self, **kwargs):
        context = super(LinkList, self).get_context_data(**kwargs)
        if context['is_paginated']:
            self.set_context_page_slice(context)
        return context

class LinkDelete(DeleteView):
    success_url = '/links/listLink/' 
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LinkDelete, self).dispatch(request, *args, **kwargs)


class TagView(ListView):
    """Show all links tags"""
    context_object_name = "tags"
    template_name = 'Links/listTags.html'
    model = Link
    paginate_by = 10
    def get_queryset(self):
        return Tag.objects.all()

    def get_context_data(self, **kwargs):
        #Call the first implementation first to get the context
        context = super(TagView, self).get_context_data(**kwargs)
        #Add in the tag that was requested
        #context['requested_tag'] = self.args[0]
        return context

class UserProfileDetailView(DetailView):
    slug_field = "username"
    template_name = 'users/user_profile.html'

    def get_user(self):
        return get_object_or_404(User, **self.kwargs)

    def get_queryset(self):
        self.user = self.get_user()
        return self.user

    def get_object(self, queryset=None):
        user=super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user



class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/edit_user_profile.html'
    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={'slug':self.request.user})

class MyLinks(UserProfileDetailView):
    template_name = 'users/user_links.html'
    def get_user(self):
        return self.request.user

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserProfile, self).dispatch( *args, **kwargs)
