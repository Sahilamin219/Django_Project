from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# cascade meaning if user is deleted then delete user's profile
	image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	# this is a method that gets run after our models get saved
	# it already exit in our models class bujt we are adding it to add some of our own functionality
	def save(self, *args, **kwargs):
		# super(Profile,self).save(*args, **kwargs)
		super().save()

		img=Image.open(self.image.path)
		# max resize pixel is around 125
		if(img.height>300 or img.width>300):
			output_size=(300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)