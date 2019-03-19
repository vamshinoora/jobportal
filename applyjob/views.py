from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import ApplyJobForm
from django.core.exceptions import PermissionDenied
# Create your views here.


class ApplyJobCreateView(CreateView):
    form_class = ApplyJobForm
    success_url = reverse_lazy('home')
    template_name = 'applyjob.html'

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)

# Create your views here.
