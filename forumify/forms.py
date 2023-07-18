from django import forms
from .models import Comment, Topic


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

