from django.urls import path
from .views import ApplyJobCreateView



app_name = 'applyjob'
urlpatterns = [
    path(' ', ApplyJobCreateView.as_view(), name='applyjob'),
]
