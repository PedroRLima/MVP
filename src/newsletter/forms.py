from django import forms 
from .models import Signup

class SignupForm(forms.ModelForm):
	class Meta:
		model = Signup
		fields = ['full_name','email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		print extension

		if not domain == 'gmail'	 or not domain == 'outlook':
			raise forms.ValidationError('Please enter a email from gmail or outlook')
		if not extension == 'com': #or not extension == 'com.br':
			raise forms.ValidationError('Please enter a valid email')

		return email 