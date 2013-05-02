# Forms here
from django import forms
from bootstrap_toolkit.widgets import BootstrapTextInput, BootstrapDateInput
from .models import Link
from taggit.forms import *
class LinkForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre del enlace'}), label="Nombre")
    tags = TagField(label="Etiquetas")
    description = forms.CharField(label="Descripcion", required=False)
    linkURL = forms.CharField(label="URL del enlace")
    class Meta:
        model = Link
        
    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {'required':'Debe escribir un nombre para el enlace.'}
        self.fields['tags'].error_messages = {'required':'Estas etiquetas le ayudan a categorizar su contenido.'}
        self.fields['linkURL'].error_messages = {'required':'Se requiere un enlace'}
        
