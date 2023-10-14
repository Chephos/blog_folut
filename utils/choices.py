from django.db import models


class CategoryChoices(models.TextChoices):
    TECHNOLOGY = "Technology", "Technology"
    TRAVEL = "Travel", "Travel"
    FOOD = "Food", "Food"
    LIFESTYLE = "Lifestyle", "Lifestyle"
    FITNESS = "Fitness", "Fitness"
    ENTERTAINMENT = "Entertainment", "Entertainment"
    INSPIRATION = "Inspiration", "Inspiration"
