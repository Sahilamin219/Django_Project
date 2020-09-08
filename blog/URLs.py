from django.urls import path
from .views import PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, add_comment_to_post
from . import views

urlpatterns=[
	# path('admin/',admin.site.urls)
	#admin.site.urls is thhe view that gets run when we go to 'admin/'
	#but at home page we can leave it empty path and the view can be views.home is the
	#function that we create at views.py that return Httresponse..
	# path('', views.home, name='blog-home'),
	path('', PostListView.as_view(), name='blog-home'),
	# to acess class as a view we can not directly write it ..have to convert it into views using .as_views()
	# <app>/<model>_<viewtype>.html

	path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),

	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),# pk:primary key
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


	#above '' is an empty route and its so becasue in urls.py the include thing have chopped off the string that has been porcessed so
	# there nothing left and then we navigate to views.home after matching empty strings
	path('about/', views.about, name='blog-about'),

	path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
	path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
	
]