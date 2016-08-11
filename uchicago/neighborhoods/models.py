from __future__ import unicode_literals

from django.db import models

# Create your models here.
class neighborhoodCHI(models.Model):
	dnaurl = models.CharField(max_length=255, default='', blank=False, null=False)
	name = models.CharField(max_length=255, default='', blank=False, null=False)

	def __unicode__(self):
		return self.name
