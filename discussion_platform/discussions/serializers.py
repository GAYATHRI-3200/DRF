from rest_framework import serializers
from .models import Discussion, Hashtag

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'name']

class DiscussionSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Discussion
        fields = ['id', 'user', 'text', 'image', 'hashtags', 'created_on']
