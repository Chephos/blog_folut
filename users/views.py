from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms
from . import workers

# Create your views here.


class Register(View):
    def post(self, request):
        form = forms.Register(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"))
        return render(request, "users/register.html", {"form": form})

    def get(self, request):
        form = forms.Register()
        return render(request, "users/register.html", {"form": form})


class UserDetailView(View):
    def get(self, request, username):
        user = workers.UserWorker.get_user_by_username(username)
        user_posts = workers.UserWorker.get_user_posts(user)
        user_comments = workers.UserWorker.get_user_comments(user)
        return render(
            request,
            "users/detail.html",
            {"user": user, "user_posts": user_posts, "user_comments": user_comments},
        )


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.ProfileUpdateForm(instance=request.user)
        return render(request, "users/update.html", {"form": form})

    def post(self, request):
        form = forms.ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
            return redirect(
                "users:user_detail", username=request.user.username
            )
        return render(request, "users/update.html", {"form": form})
