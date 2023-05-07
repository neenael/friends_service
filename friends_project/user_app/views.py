from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from user_app.models import FriendshipRequest, Friendship
from django.db.models import Q


class ServiceLoginView(LoginView):
    template_name = 'user_app/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('user_app:account', kwargs={'pk': self.request.user.pk})


class RegisterCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "user_app/sign_up.html"

    def get_success_url(self):
        return reverse_lazy('user_app:account', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response


@login_required
def account_view(request, pk):
    if request.method == 'GET':
        context = {
            "user": User.objects.get(pk=pk),
        }
        if request.user.id == pk:
            context["friends"] = Friendship.objects.filter(Q(member_1=request.user.id) | Q(member_2=request.user.id))
            context["in_reqs"] = FriendshipRequest.objects.filter(request_to=request.user.id, is_received=False).all()
            context["out_reqs"] = FriendshipRequest.objects.filter(request_from=request.user.id, is_received=False).all()
            return render(request, 'user_app/my_account.html', context=context)
        else:
            are_friends = (Friendship.objects.filter(member_1_id=request.user.id, member_2=pk).exists() or
                    Friendship.objects.filter(member_1_id=pk, member_2=request.user.id).exists())
            is_req_sent = FriendshipRequest.objects.filter(
                request_from_id=request.user.id,is_received=False, request_to_id=pk).exists()
            is_req_received = FriendshipRequest.objects.filter(
                request_from_id=pk, is_received=False, request_to_id=request.user.id).exists()

            if are_friends:
                context["status"] = "friends"
            elif is_req_sent:
                context["status"] = "request_is_sent"
            elif is_req_received:
                context["status"] = "request_is_received"
            else:
                context["status"] = "strangers"

            return render(request, 'user_app/foreign_account.html', context=context)

    if request.method == 'POST':
        if request.POST.get("send_request"):
            sent_request = FriendshipRequest.objects.get_or_create(
                request_from=User.objects.get(pk=request.user.id),
                request_to=User.objects.get(pk=pk))

            received_request = FriendshipRequest.objects.filter(
                request_from=User.objects.get(pk=pk),
                request_to=User.objects.get(pk=request.user.id))

            is_in_request = received_request.exists()
            if is_in_request:
                sent_request = sent_request[0]
                received_request = FriendshipRequest.objects.get(
                    request_from=User.objects.get(pk=pk),
                    request_to=User.objects.get(pk=request.user.id))
                sent_request.is_received = True
                received_request.is_received = True

                sent_request.save(update_fields=["is_received"])

                received_request.save(update_fields=["is_received"])

                Friendship.objects.get_or_create(
                    member_1=User.objects.get(pk=pk),
                    member_2=User.objects.get(pk=request.user.id)
                )
        elif request.POST.get("cancel_request"):
            friends_request = FriendshipRequest.objects.get(
                request_from=User.objects.get(pk=request.user.id),
                request_to=User.objects.get(pk=pk))
            friends_request.delete()
        elif request.POST.get("accept_request"):
            friends_request = FriendshipRequest.objects.get(
                request_from=User.objects.get(pk=pk),
                request_to=User.objects.get(pk=request.user.id))
            friends_request.is_received = True
            friends_request.save(update_fields=["is_received"])

            Friendship.objects.get_or_create(
                member_1=User.objects.get(pk=pk),
                member_2=User.objects.get(pk=request.user.id)
            )
        elif request.POST.get("reject_request"):
            friends_request = FriendshipRequest.objects.get(
                request_from=User.objects.get(pk=pk),
                request_to=User.objects.get(pk=request.user.id))
            friends_request.delete()
        elif request.POST.get("remove_friend"):
            friendship = Friendship.objects.filter(
                Q(member_1=request.user.id, member_2=pk) | Q(member_1=pk, member_2=request.user.id))
            friends_request = FriendshipRequest.objects.filter(
                Q(request_from=request.user.id, request_to=pk) | Q(request_from=pk, request_to=request.user.id))[0]
            friends_request.is_received = False
            friends_request.save(update_fields=["is_received"])
            friendship.delete()

        return redirect(reverse("user_app:account", kwargs={"pk": pk}))


class UsersListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_app/users_list.html'
    context_object_name = 'users'


class ServiceLogoutView(LogoutView):
    next_page = reverse_lazy("start_page")

