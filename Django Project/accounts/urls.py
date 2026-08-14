from django.urls import path
from .views import SignUpView, UserLoginView, UserLogoutView, activate_user

app_name = 'accounts'

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('activate/<int:user_pk>/<str:token>/', activate_user, name='activate'),
]