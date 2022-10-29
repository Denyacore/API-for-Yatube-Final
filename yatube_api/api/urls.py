from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register('follow', FollowViewSet, basename='follow')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')

jwt_token_patterns = [
    path('jwt/create/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(),
         name='token_verify')
]
urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include(jwt_token_patterns))
]
