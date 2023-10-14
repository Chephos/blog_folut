from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from . import workers
from . import forms

# Create your views here.


class PostDetailView(View):
    def get(self, request, post_slug):
        post = workers.Post.get_post_by_slug(post_slug)
        return render(request, "posts/detail.html", {"post": post})


class PostListView(View):
    def get(self, request):
        published_posts = workers.Post.get_published_posts()
        return render(request, "posts/list.html", {"published_posts": published_posts})


class PostCreateView(View):
    def get(self, request):
        form = forms.PostCreateForm()
        return render(request, "posts/create.html", {"form": form})

    def post(self, request):
        form = forms.PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = workers.Post.create_post(request.user, **form.cleaned_data)
            return redirect("posts:post_detail", post_slug=post.slug)

        return render(request, "posts/create.html", {"form": form})


class PostUpdateView(View):
    def get(self, request, post_slug):
        post = workers.Post.get_post_by_slug(post_slug)
        form = forms.PostUpdateForm(instance=post)
        return render(request, "posts/update.html", {"form": form, "post": post})

    def post(self, request, post_slug):
        post = workers.Post.get_post_by_slug(post_slug)
        form = forms.PostUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            workers.Post.update_post(post_slug, **form.cleaned_data)
            return render(request, "posts/detail.html", {"post": post})
        return render(request, "posts/update.html", {"form": form, "post": post})


class PostDeleteView(View):
    def get(self, request, post_slug):
        post = workers.Post.get_post_by_slug(post_slug)
        return render(request, "posts/delete.html", {"post": post})

    def post(self, request, post_slug):
        workers.Post.delete_post(post_slug)
        return redirect("posts:post_list")
