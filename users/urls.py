from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = "users"
urlpatterns = [
    path("register", views.Register.as_view(), name="register"),
    # path("", include("django.contrib.auth.urls")),

    # path(
    #     "password-change/",
    #     auth_views.PasswordChangeView.as_view(
    #         template_name="registration/custom_password_change_form.html"
    #     ),
    #     name="password_change",
    # ),
    # path(
    #     "password-change/done/",
    #     auth_views.PasswordChangeDoneView.as_view(
    #         template_name="registration/custom_password_change_done.html"
    #     ),
    #     name="password_change_done",
    # ),
    # path(
    #     "password-reset/",
    #     auth_views.PasswordResetView.as_view(
    #         template_name="registration/custom_password_reset_form.html"
    #     ),
    #     name="password_reset",
    # ),
    # path(
    #     "password-reset/done/",
    #     auth_views.PasswordResetDoneView.as_view(
    #         template_name="registration/custom_password_reset_done.html"
    #     ),
    #     name="password_reset_done",
    # ),
    # path(
    #     "password-reset/<uidb64>/<token>/",
    #     auth_views.PasswordResetConfirmView.as_view(
    #         template_name="registration/custom_password_reset_confirm.html"
    #     ),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "password-reset/complete/",
    #     auth_views.PasswordResetCompleteView.as_view(
    #         template_name="registration/custom_password_reset_complete.html"
    #     ),
    #     name="password_reset_complete",
    # ),
    path("user/<str:username>/", views.UserDetailView.as_view(), name="user_detail"),
    path("update/user/", views.ProfileUpdateView.as_view(), name="profile_update"),
]
