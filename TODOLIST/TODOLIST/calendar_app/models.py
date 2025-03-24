from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Reference CustomUser
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)  # Add due_date field
    completed = models.BooleanField(default=False)      # Add completed field

    def __str__(self):
        return self.title
