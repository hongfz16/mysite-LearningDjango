from django.db import models

from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=100)
	content=models.TextField()
	create_at=models.DateTimeField(default=timezone.now)

class Reply(models.Model):
	post=models.ForeignKey('Post',related_name='replies',related_query_name='reply')
	author=models.ForeignKey('auth.User')
	created_at=models.DateTimeField(default=timezone.now)
	content=models.TextField()