from django.shortcuts import render
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
		name = form.cleaned_data.get('full_name')
		if not name:
			name = "User" + str(randint(1,1000)

			

	context = {
		'title': title, 
		'form':form,
	}
	return render(request, 'forms.html', context)