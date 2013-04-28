# Forms here
from django import forms
from bootstrap_toolkit.widgets import BootstrapTextInput, BootstrapDateInput
from .models import Links
from django.contrib.admin.util import help_text


class LinkForm(forms.ModelForm):
    class Meta:
        model = Links
#    name = forms.CharField(help_text=u'Nombre para el enlace',)
#    description = forms.CharField(required=False, widgets=forms.Textarea)
#    linkUrl = forms.URLField()
#    date_posted = forms.DateTimeField(widget=BootstrapDateInput)
