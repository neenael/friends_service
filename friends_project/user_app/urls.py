from django.urls import path
from user_app.views import (
    RegisterCreateView,
    ServiceLoginView,
    ServiceLogoutView,
    UsersListView,
    account_view,
)

app_name = "user_app"

urlpatterns = [
    path("login/", ServiceLoginView.as_view(), name="login"),
    path("sign_up/", RegisterCreateView.as_view(), name="sign_up"),
    path("<int:pk>/", account_view, name="account"),
    path("list/", UsersListView.as_view(), name="users_list"),
    path("logout/", ServiceLogoutView.as_view(), name="logout"),
]
