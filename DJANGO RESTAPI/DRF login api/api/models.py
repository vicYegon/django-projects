from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(unique=True, null=True, max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username