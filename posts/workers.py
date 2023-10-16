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

    @staticmethod
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
    def create_post(
        user, title, subtitle, cover_photo, content, category, tags, is_published
    ):
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
            is_published=is_published,
            tags=tags,
        )
        return post

    @staticmethod
    def update_post(
        post_slug: str,
        title: str,
        subtitle: str,
        cover_photo,
        content: str,
        category: str,
        tags,
        is_published: bool,
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
        post.is_published = is_published
        post.tags = post.tags.add(*tags)
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

    @staticmethod
    def get_published_posts():
        return models.Post.objects.filter(is_published=True)


class Comment:
    @staticmethod
    def get_active_comments_for_post(post):
        return post.comments.filter(is_active=True)
    
    @staticmethod
    def get_comment_by_id(comment_id: int):
        """
        Gets comment by id
        :param comment_id: id of the comment
        :return: comment
        :raises: Http404
        """
        comment = get_object_or_404(models.Comment, id=comment_id)
        return comment
    
    @staticmethod
    def get_post_by_comment_id(comment_id):
        comment = Comment.get_comment_by_id(comment_id)
        return comment.post

    @staticmethod
    def delete_comment(comment_id: int):
        """
        Deletes a comment
        :param comment_id: id of the comment
        :return: None
        """
        comment = Comment.get_comment_by_id(comment_id)
        comment.delete()
