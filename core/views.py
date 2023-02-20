from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, JobPostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .models import JobPost


# Create your views here.

@login_required(login_url='/login/')
def index(request):
	jobs = JobPost.objects.all()
	q = request.GET.get('Q')

	if q is not None:
		jobs = JobPost.objects.filter(
			Q(description__icontains=q) |
			Q(post__icontains=q)
		)

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
# @permission_required('core.add_post', login_url='login', raise_exception=True)
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
def update_post(request, pk):
	post_update = JobPost.objects.get(host=pk)
	form = JobPostForm(instance=post_update)

	if request.user != post_update.host:
		return HttpResponse("You're not allowed here ..!")

	if request.method == 'POST':
		post_update.host = request.user
		post_update.post = request.POST['post']
		post_update.resume = request.FILES['resume']
		post_update.exp = request.POST['experience']
		post_update.desc = request.POST['description']

		# new_post = JobPost.objects.get_or_create(host=host, post=post, resume=resume, experience=exp, description=desc)
		post_update.save()

		return redirect('/')

	context = {'form': form}
	return render(request, "core/job_post.html", context=context)


@login_required(login_url='/login/')
def delete_post(request, pk):
	if request.method == 'POST':
		post = JobPost.objects.get(host=pk)
		post.delete()
	return redirect('home')


@login_required(login_url='/login/')
def user_profile(request, pk):
	user_info = JobPost.objects.get(host=pk)

	context = {'user': user_info}
	return render(request, 'core/user_profile.html', context=context)


@login_required(login_url='/login/')
def log_out(request):
	logout(request)
