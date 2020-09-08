from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
class PostForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User 
		fields = ['username']
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment 
		# fields = ['author', 'text']
		fields = ['text']
