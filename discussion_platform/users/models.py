from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username


class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following_set', on_delete=models.CASCADE)
    followed = models.ForeignKey(CustomUser, related_name='follower_set', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')
