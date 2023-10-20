from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.constants import BaseModel

# Create your models here.


class User(AbstractUser, BaseModel):
    bio = models.TextField(max_length=500, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos", default="profile_photos/big.jpg", blank=True)

    def __str__(self):
        return self.username
