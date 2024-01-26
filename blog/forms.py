from .models import Comment, Session
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for creating a new comment
    """
    class Meta:
        model = Comment
        fields = ('body',)


class SessionForm(forms.ModelForm):
    """
    Form for submitting a new session into session model
    """
    class Meta:
        model = Session
        fields = ('author', 'name', 'venue', 'length', 'profit_loss', 'notes',)