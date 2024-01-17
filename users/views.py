from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in
            return redirect("chat_room_list")  # Redirect to a home page or other appropriate page
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})
