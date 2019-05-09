from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return ('view_blog_post', None, {'title': self.title})


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
