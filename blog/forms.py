from .models import Comment, Session
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('author', 'name', 'venue', 'length', 'profit_loss', 'notes',)