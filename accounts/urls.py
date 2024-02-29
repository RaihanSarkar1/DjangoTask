from django import views
from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path("login", views.login_user, name="index"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout, name="logout"),
    path("signup", views.signup, name="signup"),
]