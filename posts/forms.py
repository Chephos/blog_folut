from django import forms
from django.utils import timezone

from . import models


class PostCreateForm(forms.ModelForm):
    published_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

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
            cleaned_data["published_at"] = timezone.now()

        return cleaned_data


class PostUpdateForm(PostCreateForm):
    pass


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            "content",
        ]
        labels = {"content": ("")}
        widgets = {
            "content": forms.TextInput(),
        }

    def clean_content(self):
        content = self.cleaned_data["content"]
        if content == "":
            raise forms.ValidationError("You must say something :)")
        return content
