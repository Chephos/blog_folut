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
    # path(
    #     "<slug:post_slug>/publish/",
    #     views.PublishPostview.as_view(),
    #     name="publish_post_view",
    # ),
]
