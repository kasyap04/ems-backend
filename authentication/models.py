from django.db import models
from django.contrib.auth.models import User

class DynamicField(models.Model):
    label = models.CharField(max_length=100)
    input_type = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)

class Employee(models.Model):
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
