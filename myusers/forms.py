# we are going to create a first uesr form that inherites from the user creation form (django)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	# email = forms.EmailField(required=True)
	email = forms.EmailField()

	class Meta:
		model = User #bcuz when ever this forms validates its going to create a new user
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User 
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile 
		fields = ['image']
