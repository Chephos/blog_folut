from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse

from . import workers
from . import forms
from . import helpers

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


class PostCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.PostCreateForm()
        return render(request, "posts/create.html", {"form": form})

    def post(self, request):
        form = forms.PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = workers.Post.create_post(request.user, **form.cleaned_data)
            return redirect("posts:post_detail", post_slug=post.slug)

        return render(request, "posts/create.html", {"form": form})


class PostUpdateView(LoginRequiredMixin, View):
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


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_slug):
        post = workers.Post.get_post_by_slug(post_slug)
        return render(request, "posts/delete.html", {"post": post})

    def post(self, request, post_slug):
        workers.Post.delete_post(post_slug)
        return redirect("posts:post_list")


class CommentCreateView(LoginRequiredMixin, View):
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


class CommentDeleteView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        post = workers.Comment.get_post_by_comment_id(comment_id)
        workers.Comment.delete_comment(comment_id)
        return redirect("posts:post_detail", post_slug=post.slug)


class LikePostView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        helpers.toggle_like_for_post(request.user, post_id)
        post = workers.Post._get_post_by_id(post_id)
        likes_count = post.likes.count()
        dislikes_count = post.dislikes.count()
        return JsonResponse(
            {"likes_count": likes_count, "dislikes_count": dislikes_count}
        )


class LikeCommentView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        helpers.toggle_like_for_comment(request.user, comment_id)
        comment = workers.Comment.get_comment_by_id(comment_id)
        likes_count = comment.likes.count()
        dislikes_count = comment.dislikes.count()
        return JsonResponse(
            {"likes_count": likes_count, "dislikes_count": dislikes_count}
        )


class DislikePostView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        helpers.toggle_dislike_for_post(request.user, post_id)
        post = workers.Post._get_post_by_id(post_id)
        dislikes_count = post.dislikes.count()
        likes_count = post.likes.count()
        return JsonResponse(
            {"dislikes_count": dislikes_count, "likes_count": likes_count}
        )


class DislikeCommentView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        helpers.toggle_dislike_for_comment(request.user, comment_id)
        comment = workers.Comment.get_comment_by_id(comment_id)
        dislikes_count = comment.dislikes.count()
        likes_count = comment.likes.count()
        return JsonResponse(
            {"dislikes_count": dislikes_count, "likes_count": likes_count}
        )
