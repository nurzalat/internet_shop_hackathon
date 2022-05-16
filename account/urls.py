from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from account import views

urlpatterns = [
    path('register/', views.RegistrationApiView.as_view()),
    path('activate/<uuid:activation_code>', views.ActivationView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('change-password/', views.NewPasswordView.as_view()),
    path('reset-password/', views.ResetPasswordView.as_view()),
]
