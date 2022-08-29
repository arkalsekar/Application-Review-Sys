from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name='contact'),
    path("check_status", views.check_status, name='check_status'),
    path("get_status", views.get_status, name='get_status'),
    path("signup", views.signup, name='signup'),
    path("login", views.handle_login, name='handle_login'),
    path("logout", views.handle_logout, name='logout'), 


]
