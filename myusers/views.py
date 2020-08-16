from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
def register(request):
	# now we have to creae a form which will pass to views
	if request.method == 'POST':
		# form = UserCreationForm(request.POST)
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			# form.save(force_insert=False)
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Accounted Has been Created! You are able to login now :)')
			# messages.success(request, f'Accounted Created for {username} !')#we have got our flashed message here
			# now we have to redirect our user to another page as his account is created
			# return redirect('blog-home')
			return redirect('login')
	else:
		# form = UserCreationForm()
		form = UserRegisterForm()
	return render(request, 'myusers/register.html', {'form': form})

# message.debug
# message.error
# message.success
# message.warning
# message.info

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			# //now give user feedback that profile has been updated and redirect them to profile page
			messages.success(request, f'Your Accounted Has been updated :)')
			return redirect('profile')
	# else:
	u_form = UserUpdateForm(instance=request.user)
	p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request, 'myusers/profile.html', context)
