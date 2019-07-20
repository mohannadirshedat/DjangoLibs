from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.decorators import login_required
from .models import Profile

#@login_required()
class CreateUser(CreateView):
    form_class = UserCreationForm
    template_name = "create_user.html"
    success_url = '/'

class ListUsers(ListView):
    model = Profile
    template_name = 'users.html'

def Home(request):
    return render(request,'dashboard.html')


class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'profile.html'