from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _
from datetime import date
from django.core.urlresolvers import reverse
# Create your models here.
class Link(models.Model):
	#__metaclass__ = models.SubfieldBase
	TAGS_SEPARATOR = ','
	#class Meta:
	 #  	verbose_name = _('link')
    #	verbose_name_plural = _('links')
    #	ordering = ('-date',)

	name = models.CharField(max_length=100)
	description = models.CharField(max_length=250, blank=True, null=True)
	linkURL = models.URLField()
	date_posted = models.DateTimeField(auto_now_add=True)
	tags = TaggableManager()
	
	
	def get_absolute_url(self):
		return reverse('detailsLink', kwargs={'pk': self.pk})#
		
		
	def __unicode__(self):
		return self.name

	def links_added_today(self):
		return self.date_posted <= date.today()

	def get_tags(self):
		tags_arr = []
		if self.tags != NULL:
			for one_tag in tags.split(self.TAGS_SEPARATOR):
				stripped_tag = one_tag.strip()
				if stripped_tag not in tags_arr:
					tags_arr.append(stripped_tag)
		return tags_arr


	
	def get_links_by_tags(self, value):
		self.tags = []	




