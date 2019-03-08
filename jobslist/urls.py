from django.urls import path
from .views import JobsCreateView,  JobDetailView, HomePageView

urlpatterns = [
    path('job/', JobsCreateView.as_view(), name='jobcreate'),
    path('jobs/detail/<int:pk>/', JobDetailView.as_view(), name='jbdetail'),

    path('', HomePageView.as_view(), name='home')


]
