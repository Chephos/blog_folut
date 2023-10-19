from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from taggit.managers import TaggableManager

from utils.constants import BaseModel
from utils import choices

# Create your models here.

User = get_user_model()


class Post(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=15000, unique=True)
    subtitle = models.CharField(max_length=150, blank=True)
    content = models.TextField(blank=True)
    cover_photo = models.ImageField(
        upload_to="cover_photos/", default="cover_photos/iba.jpg", blank=True, null=True
    )
    category = models.CharField(max_length=50, choices=choices.CategoryChoices.choices)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags = TaggableManager()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    dislikes = models.ManyToManyField(User, related_name="disliked_posts", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title[:20] + "..."

    def get_absolute_url(self, *args, **kwargs):
        return

    class Meta:
        ordering = [
            "-published_at",
        ]


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name="liked_comments")
    dislikes = models.ManyToManyField(User, related_name="disliked_comments")

    def __str__(self):
        return f"{self.author.username} commented '{self.content[:20]}'..."

    class Meta:
        ordering = [
            "-created_at",
        ]
