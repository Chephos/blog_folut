from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from . import forms
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