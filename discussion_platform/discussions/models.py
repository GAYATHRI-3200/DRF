from django.db import models
from django.conf import settings

class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Discussion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discussions')
    text = models.TextField()
    image = models.ImageField(upload_to='discussions/', null=True, blank=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='discussions')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
