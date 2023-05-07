from django.shortcuts import render, redirect
from django.urls import reverse


def start_page(request):
    if request.user.is_authenticated:
        return redirect(reverse("user_app:account", kwargs={"pk": request.user.pk}))
    return render(request, "start_page.html", {})
