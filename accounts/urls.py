from django.contrib import admin
from django.urls import path , include
from .views import CreateUser, ListUsers , Home, UpdateProfile
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', login_required(Home), name="home"),
    path('create_user/', login_required(CreateUser.as_view()), name="create_user"),
    #path('profile/<int:id>', UpdateProfile, name="profile"),
    path('users/', login_required(ListUsers.as_view()), name="users"),

]