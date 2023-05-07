from rest_framework.viewsets import ModelViewSet
from user_app.models import Friendship, FriendshipRequest
from api_app.serializers import FriendshipSerializer, FriendshipRequestSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse


@extend_schema(description="Friendship")
class FriendshipAPIViewSet(ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

    @extend_schema(
        summary="Get list of friendships",
        description="Get list of friendship",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="Not found"),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get one relationship by ID",
        description="Retrieves friendship or 404 if not found",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="This friendship not found"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Creates new friendship",
        description="Creates new friendship with post request",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="This friendship not found"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Updates friendship",
        description="Updates existing friendship with put request",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="This friendship not found"),
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Partial update",
        description="Updates existing friendship with patch request",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="This friendship not found"),
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Removes friendship",
        description="Removes existing friendship with delete request",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="This friendship not found"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


@extend_schema(description="Friendship request")
class FriendshipRequestAPIViewSet(ModelViewSet):
    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer

    @extend_schema(
        summary="Get list of friendship-requests",
        description="Get list of all friendship-requests",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="Not found"),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get one friendship-request by ID",
        description="Retrieves friendship-request or 404 if not found",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="This friendship-request not found"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Creates new friendship",
        description="Creates new friendship-request with post-request",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="This friendship-request not found"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Updates friendship-request",
        description="Updates existing friendship-request with put-request",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="This friendship-request not found"),
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Partial update of friendship-request",
        description="Updates existing friendship-request with patch request",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="This friendship-request not found"),
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Removes friendship-request",
        description="Removes existing friendship-request with delete request",
        responses={
            200: FriendshipSerializer,
            404: OpenApiResponse(description="This friendship-request not found"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
