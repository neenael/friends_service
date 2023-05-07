from rest_framework.serializers import ModelSerializer
from user_app.models import Friendship, FriendshipRequest


class FriendshipSerializer(ModelSerializer):
    class Meta:
        model = Friendship
        fields = "__all__"


class FriendshipRequestSerializer(ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = "__all__"
