from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CustomUser, Follow
from .serializers import CustomUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def follow_user(self, request, pk=None):
        user = self.get_object()
        if request.user == user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follow, created = Follow.objects.get_or_create(follower=request.user, followed=user)
        if not created:
            return Response({"detail": "You are already following this user."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": f"You are now following {user.username}."}, status=status.HTTP_201_CREATED)

    def unfollow_user(self, request, pk=None):
        user = self.get_object()
        if request.user == user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follow = Follow.objects.filter(follower=request.user, followed=user).first()
        if not follow:
            return Response({"detail": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)

        follow.delete()
        return Response({"detail": f"You have unfollowed {user.username}."}, status=status.HTTP_200_OK)
