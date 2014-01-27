from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext

from taggit.managers import TaggableManager

# Create your models here.
class Link(models.Model):
	#__metaclass__ = models.SubfieldBase
	TAGS_SEPARATOR = ','

	class Meta:
		"""docstring for Meta"""
		verbose_name=u'link'
		verbose_name_plural=u'links'
		ordering= ['-date_posted']

	name = models.CharField(max_length=100)
	description = models.CharField(max_length=250, blank=True, null=True)
	linkURL = models.URLField()
	date_posted = models.DateTimeField(auto_now_add=True)
	tags = TaggableManager()
	posted_by = models.CharField(max_length=15)
		
	
	def get_absolute_url(self):
		return reverse('detailsLink', kwargs={'pk': self.pk})
		
	def posted_by_username(self):
		try:
			return User.objects(user__username=self.posted_by)
		except User.DoesNotExist:
			return None
	
	def __unicode__(self):
		return self.name

	def links_added_today(self):
		return Link.objects.filter(date_posted__day=date.today()) 

	def get_tags(self):
		tags_arr = []
		if self.tags != NULL:
			for one_tag in tags.split(self.TAGS_SEPARATOR):
				stripped_tag = one_tag.strip()
				if stripped_tag not in tags_arr:
					tags_arr.append(stripped_tag)
		return tags_arr

class UserProfile(models.Model):
	"""managing Users Profiles"""
	user = models.OneToOneField(User, unique=True)
	url = models.URLField("Website", blank=True)
	company = models.CharField(max_length=50, blank=True)
	bio = models.TextField(null=True)

	def __unicode__(self):
		return "Perfil de %s" % self.user
	def create_profile(sender, instance, created, **kwargs):
		if created:
			profile, created = UserProfile.objects.get_or_create(user=instance)

	from django.db.models.signals import post_save
	post_save.connect(create_profile, sender=User)
		

