from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
# Create your models here.
class ApplyJob(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=30)
    phoneno = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    collage = models.CharField(max_length=1000, null=False, blank=False)
    percentage = models.IntegerField(default=0)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    experience = models.IntegerField(default=0,
                                     validators=[MinValueValidator(0), MaxValueValidator(4)])
    skills = models.CharField(max_length=50, null=False, blank=False)


