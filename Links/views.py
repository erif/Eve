# Create your views here.
import datetime
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
        min_slice = 10
        
        
        
        
#class LinkDelete(DeleteView):