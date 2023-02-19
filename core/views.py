from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, JobPostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import JobPost


# Create your views here.

@login_required(login_url='/login/')
def index(request):
	jobs = JobPost.objects.all()
	context = {'jobs': jobs}

	return render(request, 'core/index.html', context=context)


def sign_up(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)

			return redirect('/home')

	context = {'form': form}
	return render(request, 'registration/signup.html', context=context)


@login_required(login_url='/login/')
def job_post(request):
	form = JobPostForm()
	if request.method == 'POST':
		host = request.user
		post = request.POST['post']
		resume = request.FILES['resume']
		exp = request.POST['experience']
		desc = request.POST['description']

		new_post = JobPost.objects.create(host=host, post=post, resume=resume, experience=exp, description=desc)
		new_post.save()

		return redirect('/')

	context = {'form': form}
	return render(request, 'core/job_post.html', context=context)


@login_required(login_url='/login/')
def log_out(request):
	logout(request)
