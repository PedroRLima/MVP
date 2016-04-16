from django.db import models

# Create your models here.
class Signup(models.Model):
	full_name = models.CharField(max_length=200, blank=False, null=False)
	email     = models.EmailField(blank=False, null=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.email 
