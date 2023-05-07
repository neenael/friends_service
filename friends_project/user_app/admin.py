from django.contrib import admin
from user_app.models import FriendshipRequest, Friendship

admin.site.register(FriendshipRequest)
admin.site.register(Friendship)
