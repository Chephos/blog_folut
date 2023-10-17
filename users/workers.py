from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from . import models

User = get_user_model()


class UserWorker:
    @staticmethod
    def get_user_by_username(username):
        user = get_object_or_404(User, username=username)
        return user

    @staticmethod
    def get_user_posts(user):
        return user.posts.filter(is_published=True)

    @staticmethod
    def get_user_comments(user):
        return user.comments.filter(is_active=True)

    @staticmethod
    def get_user_posts_and_comments(username):
        user = UserWorker.get_user_by_username(username)
        posts = UserWorker.get_user_posts(user)
        comments = UserWorker.get_user_comments(user)
        return [posts, comments]
