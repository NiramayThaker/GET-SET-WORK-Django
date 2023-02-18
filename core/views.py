from django.shortcuts import render, HttpResponse
from .forms import RegistrationForm


# Create your views here.
def index(request):
	return render(request, 'core/index.html')


def sign_up(request):
	form = RegistrationForm()
	if request.method == 'POST':
		pass

	context = {'form': form}
	return render(request, 'registration/signup.html', context=context)
