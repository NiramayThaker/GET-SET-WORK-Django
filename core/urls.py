from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='home'),
	path('home', views.index, name='home'),
	path('sign-up', views.sign_up, name='sign-up'),
	path('logout', views.log_out, name='log-out'),
	path('job-post', views.job_post, name='job-post'),
	path('update-post/<str:pk>/', views.update_post, name='update-post'),
	path('delete-post/<str:pk>/', views.delete_post, name='delete-post'),
]
