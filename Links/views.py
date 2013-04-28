# Create your views here.
from django.views.generic import TemplateView, ListView
from .forms import LinkForm
from django.http import HttpResponseRedirect

class Index(TemplateView):
    template_name = 'Links/index.html'

class About(TemplateView):
    template_name = 'Links/about.html'
    
class AddLink(TemplateView):
    template_name = 'Links/addLink.html'
    LinkForm = LinkForm
    def post(self, request, *args, **kwargs):
        link_form = LinkForm(request.POST)
        if link_form.is_valid():
            link_form.save()
            return HttpResponseRedirect(reverse('something'))
        else:
            return self.get(request, link_form=link_form, *args, **kwargs)
class LinkList(ListView):
    template_name = 'Links/listLink'
    paginate_by = 10
    
class LastLinks(ListView):
  def get_queryset(self):
    return Link.objects.filter(indexed_datetime__lte=datetime.now())