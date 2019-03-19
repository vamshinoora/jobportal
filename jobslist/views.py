from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .models import JobsModel
# from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse
# Create your views here.


class HomePageView(LoginRequiredMixin, ListView):
    login_url = '/users/login/'
    redirect_field_name = 'login'
    model = JobsModel
    template_name = 'home.html'
    context_object_name = 'jobs_list'


class JobsCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login/'
    redirect_field_name = 'login'
    model = JobsModel
    template_name = 'jbcreate.html'
    fields = '__all__'

    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.is_superuser:
            print(self.request.user.is_superuser)
            raise PermissionDenied 

        return super().dispatch(request, *args, **kwargs)


# class JobsListView(LoginRequiredMixin, ListView):
#     login_url = '/users/login/'
#     redirect_field_name = 'login'
#     model = JobsModel
#     template_name = 'jblist.html'
#
#     context_object_name = 'jobs_list'


class JobDetailView(LoginRequiredMixin, DetailView):
    login_url = '/users/login/'
    redirect_field_name = 'login'
    model = JobsModel
    template_name = 'jbdetail.html'
