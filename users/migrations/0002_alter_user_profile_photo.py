# Generated by Django 4.2.6 on 2023-10-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(
                blank=True, default="profile_photos/big.jpg", upload_to="profile_photos"
            ),
        ),
    ]
