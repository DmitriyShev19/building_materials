from django import forms
from .models import Comment, Feedback


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'message',)
