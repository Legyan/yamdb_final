from django.urls import include, path
from rest_framework import routers

from api.views import (CategoryViewSet,
                       CommentViewSet,
                       GenreViewSet,
                       get_token,
                       ReviewViewSet, signup_user, TitleViewSet,
                       UserViewset)


router_v1 = routers.DefaultRouter()

router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router_v1.register('users', UserViewset, basename='users')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', signup_user),
    path('v1/auth/token/', get_token),
]
