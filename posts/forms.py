from django import forms

from . import models


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            "title",
            "subtitle",
            "content",
            "cover_photo",
            "category",
            "tags",
            "is_published",
        ]

    def clean(self):
            cleaned_data = super().clean()
            is_published = cleaned_data.get("is_published")
            content = cleaned_data.get("content")

            if is_published is True:
                if content == "":
                    raise forms.ValidationError("Content is required")

            return cleaned_data


class PostUpdateForm(PostCreateForm):
    pass

    # def clean_content(self):
    #     content = self.cleaned_data.get("content")
    #     if not content:
    #         raise forms.ValidationError("Content is required")
