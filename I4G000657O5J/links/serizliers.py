from django.db import models
from .models import Link

class Meta(models.Model):
    model = Link
    field = "__all__"
