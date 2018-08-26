from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm


class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('core:movie_list')

