from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from django.core.exceptions import PermissionDenied
# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
