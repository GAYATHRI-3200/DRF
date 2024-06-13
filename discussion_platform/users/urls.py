from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('users/<int:pk>/follow/', UserViewSet.as_view({'post': 'follow_user'}), name='user-follow'),
    path('users/<int:pk>/unfollow/', UserViewSet.as_view({'post': 'unfollow_user'}), name='user-unfollow'),
]

urlpatterns += router.urls
