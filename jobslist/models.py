from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
# Create your models here.


class JobsModel(models.Model):
    JobTitle = models.CharField(max_length=50, null=False, blank=False)
    Company = models.CharField(max_length=20, null=False, blank=False)
    DateAdded = models.DateTimeField(auto_now=True)
    Requirements = models.CharField(max_length=50, null=False, blank=False)
    Experiecne = models.IntegerField(default=0,
                                     validators=[MinValueValidator(0), MaxValueValidator(4)])
    Salary = models.IntegerField(default=150000,
                                 validators=[MinValueValidator(150000), MaxValueValidator(1300000)])
    Description = models.TextField()
    HrMail = models.EmailField(max_length=30)

    def __str__(self):
        return self.JobTitle[:20]

    def get_absolute_url(self):
        return reverse('jbdetail', args=[str(self.id)])
