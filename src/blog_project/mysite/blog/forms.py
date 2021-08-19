from django import forms
from blog.models import Comment, Post


class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ("author", "title", "text")

        widgets = {
            "title": forms.TextInput(attrs={"class": "textinputclass"}),
            "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea post_content"})
        }


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ("author", "text")

        widgets = {
            "title": forms.TextInput(attrs={"class": "textinputclass"}),
            "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea"})
        }
