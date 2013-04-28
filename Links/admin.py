from Links.models import Links
from django.contrib import admin


class LinksAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	
		
admin.site.register(Links, LinksAdmin)
