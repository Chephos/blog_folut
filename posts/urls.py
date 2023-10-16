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
]
