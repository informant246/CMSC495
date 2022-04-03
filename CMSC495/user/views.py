from django.http import request
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm


@login_required
def profileView(request):
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'user/profile.html', context=context)


def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'user/login.html')
    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {"form": form})


@login_required
def editView(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'user/profile.html')
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'user/edit.html', context=context)
