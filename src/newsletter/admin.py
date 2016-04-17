from django.contrib import admin

from .forms import SignupForm
from .models import Signup

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'timestamp', 'updated']
	form = SignupForm 
	#class Meta:
	#	form = SignupForm

admin.site.register(Signup, SignupAdmin)
