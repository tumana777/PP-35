from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail

class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        user_token = default_token_generator.make_token(user)
        activate_url = self.request.build_absolute_uri(reverse_lazy('accounts:activate', kwargs={'user_pk': user.pk, 'token': user_token}))

        send_mail('Activate your account',
                  f'Hi {user.username}, Please click on the link to activate your account: \n{activate_url}',
                  '',
                  [user.email]
        )

        return redirect('accounts:login')

def activate_user(request, user_pk, token):
    user = User.objects.get(pk=user_pk)

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Account activated successfully')
    return HttpResponse('Invalid activation link or account already activated')

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')