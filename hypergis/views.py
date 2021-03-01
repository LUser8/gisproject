from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import RegisterFarmForm


@login_required
def home(request):
    return render(request, 'hypergis/user_home.html')


def register_field(request):
    if request.method == 'POST':
        form = RegisterFarmForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(request.user)
    else:
        form = RegisterFarmForm()
    return render(request, 'hypergis/field_register.html', {'form': form})


def flight_upload(request):
    return render(request, 'hypergis/flight_upload.html')