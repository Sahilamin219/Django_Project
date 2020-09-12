from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
# Create your views here.
# posts=[
# 	{
# 	'author':'Sahil Amin',
# 	'title':'First Blog',
# 	'content':'content_1',
# 	'date_posted':'July 15, 2020'
# 	},
# 	{'author':'Sahil Amin',
# 	'title':'Second Blog',
# 	'content':'content_2',
# 	'date_posted':'July 16, 2020'
# 	}
# 	]
#this function is going to handle traffic from homepage of our blog and
#goinng to be use request argument 
def home(request):
	# context={'posts':posts}
	context = {
		'posts':Post.objects.all()
	}
	# return HttpResponse('<h1> BlogHome </h1>')
	#1. now we have to map this url
	#2. now we can render templates instead of Httpresponse
	return render(request,'blog/home.html', context)

# in our class based view we are basically just setting some variable and in our
# function view we haad to actually render a function and explicity pass in that information now
# we could have saved some few lines of code if we had used generic view default
class PostListView(ListView):
	# we create a Model which tell our list view what model to query in order to
	# create a list and in this case we want it to be all of our posts so we will set that model equal to Post
	model = Post
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	# context in our home function is a Post object but in out list view it will call that a variable object list
	# instead of post so we can either gointo our template and change it so that its looping over obejct list or we can set 
	# one more variable in our list view and let the class know that we want that varible to be called post.
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by=5


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	# ordering = ['-date_posted']
	paginate_by=5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


# when we look at an indivisual post this is going to be a detailed view
class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url='/'
	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	# return HttpResponse('<h1> Blog about </h1>')
	return render(request, 'blog/about.html', {'title':'about'})
	#now map it aslo i urlpatterns


# our urlpatterns are dirceted to certain views which are these functions and the views then handle the logic
# for the routes and then render our templates 
# Now, we have class based views which have a lot of buiult in functionality that we try to handle a lot of the 
# backend logic for us ...there are different types of class based views which are lsit views, detailed views 
# updates views, delete views

@login_required
def add_comment_to_post(request, pk, *args, **kwargs):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
    
@login_required
def comment_approve(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.approve()
	return redirect('post-detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.delete()
	return redirect('post-detail', pk=comment.post.pk)