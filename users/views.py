from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegisterForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        if u_form.is_valid():
            user = u_form.save()
            p_form = ProfileUpdateForm(request.POST, instance=user.profile)
            if p_form.is_valid():
                p_form.save()
            username = u_form.cleaned_data.get('username', '')
            messages.success(request, f'Account Created for {username}!')
            return redirect('user-home')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileUpdateForm()
    return render(request, 'users/register.html', {'u_form': u_form, 'p_form': p_form})

