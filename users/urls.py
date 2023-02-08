from . import views
from django.urls import path
from django.contrib.auth import views as auth_view


urlpatterns = [
    path("accounts/register/", views.register, name="register"),
    path("accounts/logout/", auth_view.LogoutView.as_view(
        template_name="logout.html"), name="logout"),
    path("accounts/login/", auth_view.LoginView.as_view(
        template_name="login.html"), name="login"),
    path("accounts/password_change/", auth_view.PasswordChangeView.as_view(
        template_name="password_change.html"), name="password_change"),
    path("accounts/password_change/done/", auth_view.PasswordChangeDoneView.as_view(
        template_name="password_change_done.html"), name="password_change_done",),
    path("accounts/password_reset/", auth_view.PasswordResetView.as_view(
        template_name="password_reset.html"), name="password_reset",),
    path("accounts/password_reset/done/", auth_view.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name="password_reset_done",),
    path("accounts/reset/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"), name="password_reset_confirm",),
    path("accounts/reset/done/", auth_view.PasswordChangeDoneView.as_view(
        template_name="password_reset_complete.html"), name="password_reset_complete",),
]
