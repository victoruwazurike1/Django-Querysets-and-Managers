from django.db import models
from .models import rest_framework
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.

class Link(models.Model):

    # DB Fields
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank = True, unique=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts"
    )
    
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
objects = models.Manager()
public = ActiveLinkManager()
