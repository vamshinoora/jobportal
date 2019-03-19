from django import forms
from .models import ApplyJob

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model=ApplyJob
        fields=[
            'name',
            'email',
            'phoneno',
           # 'date',
            'collage',
            'percentage',
            'gender',
            'experience',
            'skills',


        ]