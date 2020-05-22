from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """Simply a blog post."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=80)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Show post title or it's first 20 letters."""
        if len(self.title) > 20:
            return f'{self.title[:20]}...'
        else:
            return f'{self.title}'
