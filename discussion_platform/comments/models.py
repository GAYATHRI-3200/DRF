from django.db import models
from django.conf import settings
from discussions.models import Discussion

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
