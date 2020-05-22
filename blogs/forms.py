"""Classes for forms in blogs app."""

from django import forms

from .models import BlogPost

class PostForm(forms.ModelForm):
    """Create post."""
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Your brilliant thoughts'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
