# Create your views here.
import datetime
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from endless_pagination.views import AjaxListView
from django.utils import timezone
from django.core.urlresolvers import reverse
from .models import Link
from .forms import LinkForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

class Index(TemplateView):
    template_name = 'Links/index.html'

class About(TemplateView):
    template_name = 'Links/about.html'
    
class LinkAdd(CreateView):
    template_name = 'Links/addLink.html'
    model = Link
    form_class = LinkForm
    def post(self, request, *args, **kwargs):
        link_form = LinkForm(request.POST)
        if(link_form.is_valid()):
            saved_link=link_form.save()
            return HttpResponseRedirect(reverse('detailsLink', args=(saved_link.id,)))
        else:
            return self.get(request, link_form=LinkForm, *args, **kwargs)
        

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
        
        
        
#class LinkDelete(DeleteView):