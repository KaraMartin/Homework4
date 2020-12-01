from django.db import models

# Create your models here.


class Task(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)