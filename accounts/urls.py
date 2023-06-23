from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, 
    PasswordResetConfirmView, PasswordResetCompleteView,)

from . import views

urlpatterns = [
    path("signup/",views.signup, name="signup"),
    path("activate/", views.account_verification, name="activate"),
    path("reativate/", views.resend_verification_code, name='resend'),
    path("login/", view=views.login_view, name="login"),
    path("logout/", view=views.logout_view, name="logout"),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
