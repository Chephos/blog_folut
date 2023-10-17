from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.core.paginator import Paginator

from . import workers
from . import forms
from . import models

# Create your views here.


class PostDetailView(View):
    def get(self, request, post_slug):
        post = workers.Post.get_post_by_slug(post_slug)
        active_comments = workers.Comment.get_active_comments_for_post(post)
        comment_form = forms.CommentCreateForm()
        return render(
            request,
            "posts/detail.html",
            {
                "post": post,
                "form": comment_form,
                "comments": active_comments,
            },
        )


class PostListView(View):
    def get(self, request):
        published_posts = workers.Post.get_published_posts()
        paginator = Paginator(published_posts, 12)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
        return render(
            request, "posts/list.html", {"published_posts_page_obj": page_obj}
        )


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
            return redirect("posts:post_detail", post_slug=post.slug)
        return render(request, "posts/update.html", {"form": form, "post": post})


class PostDeleteView(View):
    def get(self, request, post_slug):
        post = workers.Post.get_post_by_slug(post_slug)
        return render(request, "posts/delete.html", {"post": post})

    def post(self, request, post_slug):
        workers.Post.delete_post(post_slug)
        return redirect("posts:post_list")


class CommentCreateView(View):
    def post(self, request, post_slug):
        post = workers.Post.get_post_by_slug(post_slug)
        form = forms.CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("posts:post_detail", post_slug=post.slug)
        return render(request, "posts/detail.html", {"post": post, "form": form})


class CommentDeleteView(View):
    def post(self, request, comment_id):
        post = workers.Comment.get_post_by_comment_id(comment_id)
        workers.Comment.delete_comment(comment_id)
        return redirect("posts:post_detail", post_slug=post.slug)
