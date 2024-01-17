from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("chat_room_list")  # Redirect to a home page or other appropriate page
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
