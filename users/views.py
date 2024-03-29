from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm


# from django.core.mail import send_mail


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Konto zostało utworzone. Teraz możesz się zalogować.")
            # send_mail()
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "register.html", {"form": form})
