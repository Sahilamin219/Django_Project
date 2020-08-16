from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
	title=models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	# auto_now=True ..updates time everytime(current)
	# auto_now_add=True ..specifies time of only when created
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
		
	# we need to create that "get absolute URL method" so that 
	# Django knows how to find the location to a specific post
	# redirecr returns specific route  but reverse will simply
	# return the full URL to that route as a string so that is the difference b/w those
	# and in this case we will simply return the URL string and let the view handle the 
	# redirect for us.

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})#this method requires a url for a specific post so kwargs is added