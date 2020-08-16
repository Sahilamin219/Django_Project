from django.db.models.signals import post_save
from django.contrib.auth.models import User 
# here User is the sender, import the recivers
from django.dispatch import receiver
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect



# as we want a new user profile to be created for each new user
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
# 	# if created:
# 		# Profile.objects.create(user=instance)
# 	user = instance
# 	if created:
# 		profile = UserProfile(user=user)
# 		profile.save()



# @receiver(post_save, sender=User)
# def save_profile(sender, instance,**kwargs):
# 	instance.profile.save()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	try:
		instance.profile.save()
	except ObjectDoesNotExist:
		Profile.objects.create(user=instance)
