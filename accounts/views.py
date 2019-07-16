from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile , Company


class Home(ListView):
    model =Profile
    template_name = "dashboard.html"
class ListUser(ListView):
    model = Profile
    template_name = "users.html"
