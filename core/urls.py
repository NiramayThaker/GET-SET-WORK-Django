from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='home'),
	path('home', views.index, name='home'),
	path('sign-up', views.sign_up, name='sign-up'),
	path('logout', views.log_out, name='log-out'),
	path('job-post', views.job_post, name='job-post'),
]
