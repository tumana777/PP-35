from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('accounts:login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')