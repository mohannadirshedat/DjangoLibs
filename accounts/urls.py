from django.contrib import admin
from django.urls import path , include
from .views import Home,ListUser

urlpatterns = [
    path('users', ListUser.as_view() , name="users"),
    path('', Home.as_view(), name="home"),

]