from django.db import models

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	technology = models.CharField(max_length=20)
	image = models.FilePathField(path="static/img")

	def __str__(self):
		return self.title

class Contact(models.Model):
	name = models.CharField(max_length=50, blank=False)
	email = models.EmailField(blank=False)
	message = models.TextField(blank=False)

	def __str__(self):
		return self.email