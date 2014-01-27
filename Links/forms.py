# Forms here
from django import forms

from .models import Link, UserProfile

from bootstrap_toolkit.widgets import BootstrapTextInput, BootstrapDateInput
from taggit.forms import *

class LinkForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre del enlace'}), label="Nombre")
    tags = TagField(label="Etiquetas")
    description = forms.CharField(label="Descripcion", required=False)
    linkURL = forms.CharField(label="URL del enlace")
    class Meta:
        model = Link
        exclude = 'posted_by'
        
    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {'required':'Debe escribir un nombre para el enlace.'}
        self.fields['tags'].error_messages = {'required':'Estas etiquetas le ayudan a categorizar su contenido.'}
        self.fields['linkURL'].error_messages = {'required':'Se requiere un enlace'}

class UserProfileForm(forms.ModelForm):
    """form for UserProfileForm"""
    class Meta:
        model = UserProfile
        exclude = 'user'
        
    
class DeleteLinkForm(forms.ModelForm):
	link_name = forms.ModelChoiceField(queryset=Link.objects.all(), empty_label="(Nothing)")
	class Meta:
		model = Link