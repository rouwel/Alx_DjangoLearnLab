from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserCreateForm, UserUpdaterForm


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreateForm()
    return render(request, "register.html", {"form": form})


@login_required
def profile(request):
    if request.method == 'POST':
        L_form = UserUpdaterForm(request.POST, instance=request.user)
        if L_form.is_valid():
            L_form.save()
            return redirect('profile')
    else:
        L_form= UserUpdaterForm(instance=request.user)

    return render(request, 'profile.html', {'L_form': L_form})






