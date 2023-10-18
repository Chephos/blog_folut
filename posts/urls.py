from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("list/", views.PostListView.as_view(), name="post_list"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("<slug:post_slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path(
        "<slug:post_slug>/delete/", views.PostDeleteView.as_view(), name="post_delete"
    ),
    path("<slug:post_slug>/edit/", views.PostUpdateView.as_view(), name="post_update"),
    path(
        "<slug:post_slug>/comment/",
        views.CommentCreateView.as_view(),
        name="comment_create",
    ),
    path(
        "comment/<int:comment_id>/delete/",
        views.CommentDeleteView.as_view(),
        name="comment_delete",
    ),
    path("post/like/<int:post_id>/", views.LikePostView.as_view(), name="like_post"),
    path(
        "post/dislike/<int:post_id>/",
        views.DislikePostView.as_view(),
        name="dislike_post",
    ),
    path(
        "comment/like/<int:comment_id>/",
        views.LikeCommentView.as_view(),
        name="like_comment",
    ),
    path(
        "comment/dislike/<int:comment_id>/",
        views.DislikeCommentView.as_view(),
        name="dislike_comment",
    ),
]
