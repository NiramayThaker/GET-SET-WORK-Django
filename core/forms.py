from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import JobPost


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class JobPostForm(forms.ModelForm):
	class Meta:
		model = JobPost
		fields = ['post', 'resume', 'experience', 'description']
