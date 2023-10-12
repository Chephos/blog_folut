from django.utils import timezone
from django.shortcuts import get_object_or_404

from . import models


class Post:
    @staticmethod
    def _get_post_by_id(post_id: int):
        """
        Gets post by id
        :param post_id: id of the post
        :return: post
        :raises: Http404
        """
        post = get_object_or_404(models.Post, id=post_id)
        return post

    def get_post_by_slug(post_slug: str):
        """
        Gets post by slug
        :param post_slug: slug of the post
        :return: post
        :raises: Http404
        """
        post = get_object_or_404(models.Post, slug=post_slug)
        return post

    @staticmethod
    def create_post(user, title, subtitle, cover_photo, content, category, tags):
        """
        Creates a post
        :param user: user who created the post
        :param title: title of the post
        :param subtitle: subtitle of the post
        :param cover_photo: cover photo of the post
        :param content: content of the post
        :param category: category of the post
        :param tags: tags of the post
        :return: post
        """
        post = models.Post.objects.create(
            author=user,
            title=title,
            subtitle=subtitle,
            cover_photo=cover_photo,
            content=content,
            category=category,
            tags=tags,
        )
        return post

    @staticmethod
    def publish_post(post_id: int):
        """
        Publishes a post
        :param post_id: id of the post
        :return: None
        """
        post = Post._get_post_by_id(post_id)
        if post.is_published == False:
            post.is_published = True
            post.published_at = timezone.now()
            post.save()

    @staticmethod
    def update_post(
        post_slug: str,
        title: str,
        subtitle: str,
        cover_photo,
        content: str,
        category: str,
        tags,
    ):
        """
        Updates a post
        :param post_id: id of the post
        :param title: title of the post
        :param subtitle: subtitle of the post
        :param cover_photo: cover photo of the post
        :param content: content of the post
        :param category: category of the post
        :param tags: tags of the post
        :return: None
        """
        post = Post.get_post_by_slug(post_slug)
        post.title = title
        post.subtitle = subtitle
        post.cover_photo = cover_photo
        post.content = content
        post.category = category
        post.tags = tags
        post.save()

    @staticmethod
    def delete_post(post_slug: str):
        """
        Deletes a post
        :param post_slug: slug of the post
        :return: None
        """
        post = Post.get_post_by_slug(post_slug)
        post.delete()
