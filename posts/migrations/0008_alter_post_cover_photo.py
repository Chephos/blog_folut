# Generated by Django 4.2.6 on 2023-10-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0007_comment_dislikes_comment_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="cover_photo",
            field=models.ImageField(
                blank=True,
                default="cover_photos/iba.jpg",
                null=True,
                upload_to="cover_photos/",
            ),
        ),
    ]
