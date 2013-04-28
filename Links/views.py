# Create your views here.
from django.views.generic import TemplateView, ListView
class Index(TemplateView):
    template_name = 'Links/index.html'

class About(TemplateView):
    template_name = 'Links/about_us.html'