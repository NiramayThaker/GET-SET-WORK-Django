from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class JobPost(models.Model):
	host = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.CharField(max_length=30)
	resume = models.FileField(upload_to='media/')
	upload = models.DateTimeField(auto_now_add=True)
	experience = models.DecimalField(max_digits=7, decimal_places=2)
	description = models.TextField()

	def __str__(self):
		return f"{self.host.username} | {self.post}"
