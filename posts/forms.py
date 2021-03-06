"""Post Forms."""

# Django
from django import forms

# Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post Model Form."""
    
    class Meta:
        """Form settings"""

        model = Post
        fields = ('user', 'title', 'photo')