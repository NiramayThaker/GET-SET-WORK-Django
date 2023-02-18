from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, JobPostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login/')
def index(request):
	return render(request, 'core/index.html')


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
def log_out(request):
	logout(request)


@login_required(login_url='/login/')
def job_post(request):
	form = JobPostForm()
	if request.method == 'POST':
		pass

	context = {'form': form}
	return render(request, 'core/job_post.html', context=context)
