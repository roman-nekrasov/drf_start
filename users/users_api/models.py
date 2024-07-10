from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    desiredSalary = models.IntegerField()
    grade = models.CharField(max_length=100)
    exp = models.IntegerField()
    technologies = models.JSONField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'country', 'desiredSalary', 'grade', 'exp', 'technologies']
