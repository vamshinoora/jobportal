from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


# Create your models here.

class CustomUser(AbstractUser):
    passing_year = models.PositiveIntegerField(default=2019)
