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
    cover_photo = models.ImageField(upload_to="cover_photos")
    category = models.CharField(max_length=50, choices=choices.CategoryChoices.choices)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title[:20] + "..."
