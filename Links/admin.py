from Links.models import Link
from django.contrib import admin


class LinkAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	
		
admin.site.register(Link, LinkAdmin)
