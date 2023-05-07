from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class FriendshipRequest(models.Model):
    class Meta:
        verbose_name = _("Friendship request")
        verbose_name_plural = _("Friendship requests")

    request_from = models.ForeignKey(
        User,
        related_name="sender",
        on_delete=models.CASCADE,
        verbose_name=_("Request from"),
    )
    request_to = models.ForeignKey(
        User,
        related_name="receiver",
        on_delete=models.CASCADE,
        verbose_name=_("Request to"),
    )
    is_received = models.BooleanField(default=False, verbose_name=_("Is received"))

    def __str__(self):
        return "{request_from} -> {request_to}".format(
            request_from=self.request_from, request_to=self.request_to
        )


class Friendship(models.Model):
    class Meta:
        verbose_name = _("Friendship")
        verbose_name_plural = _("Friendships")

    member_1 = models.ForeignKey(
        User,
        related_name="member_1",
        on_delete=models.CASCADE,
        verbose_name=_("Member 1"),
    )
    member_2 = models.ForeignKey(
        User,
        related_name="member_2",
        on_delete=models.CASCADE,
        verbose_name=_("Member 2"),
    )
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date created")
    )

    def __str__(self):
        return "{member_1} + {member_2}".format(
            member_1=self.member_1, member_2=self.member_2
        )
