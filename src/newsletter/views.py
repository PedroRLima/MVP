from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from random import randint

from .forms import ContactForm, SignupForm 


# Create your views here.
def home(request):

	form = SignupForm(request.POST or None)
	title = 'Welcome !'
	context = {
		'title': title,
		'form': form,
	}

	if form.is_valid():
		instance = form.save(commit=False)

		name = form.cleaned_data.get('full_name')
		if not name:
			name = "User" + str(randint(1,1000))
		instance.full_name = name 

		instance.save()
		context = {
			'title': 'Thank you for signing up'
		}

	return render(request, 'home.html', context)

def contact(request):
	title = 'Contact'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_name = form.cleaned_data.get('full_name')

		if not form_name:
			form_name = "User" + str(randint(1,1000))

		form_email   = form.cleaned_data.get('email')
		form_message = form.cleaned_data.get('message')

		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = '%s: %s via %s' % (form_name, form_message, form_email) 


		send_mail(
			subject, 
			contact_message, 
			from_email, 
			to_email, 
			fail_silently=False
			)

			

	context = {
		'title': title, 
		'form':form,
	}
	return render(request, 'forms.html', context)