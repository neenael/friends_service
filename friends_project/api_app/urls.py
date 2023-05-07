from django.urls import path, include
from api_app.views import FriendshipAPIViewSet, FriendshipRequestAPIViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"friendship", FriendshipAPIViewSet)
router.register(r"friendship_request", FriendshipRequestAPIViewSet)

app_name = "api_app"

urlpatterns = [
    path('', include(router.urls)),
]
