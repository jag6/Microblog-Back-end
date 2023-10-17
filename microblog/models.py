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
    
class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    author = models.ForeignKey(User, related_name='tags', on_delete=models.DO_NOTHING)
    posts = models.ManyToManyField(Post, related_name='tags', blank=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    created_on = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.body

class Like(models.Model):
    liker = models.ForeignKey(User, related_name='likes', on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_on = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.liker