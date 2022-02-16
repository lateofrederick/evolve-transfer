from django.shortcuts import render, redirect
from evolve_transfer.forms.register_form import RegisterUserForm
from django.contrib.auth import login
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        breakpoint()
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("homepage")
        messages.error(request, "Provide valid information")
    form = RegisterUserForm()
    return render(request, "signup/register.html", {"form": form})
