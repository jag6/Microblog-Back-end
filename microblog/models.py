from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    body = models.TextField(null=True)
    image = models.ImageField(upload_to='posts/', blank=True)
    created_on = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
	    return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    created_on = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        ordering = ['created_on']