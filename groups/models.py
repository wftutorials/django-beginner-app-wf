from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Groups(models.Model):
    name = models.CharField(max_length=50, blank=True,help_text="Group Name")
    description = models.TextField(help_text="Add a description")
    author = models.TextField(help_text="Choose an Author")
    status = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

class Members(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
