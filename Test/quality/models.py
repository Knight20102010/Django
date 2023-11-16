from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="post_author")