from django.urls import path
from .views import signup , user_activate
from django.contrib.auth import views as auth_views

app_name = 'User'

urlpatterns = [
    path('signup/',signup , name = 'signup'),
    path('<str:username>/activate',user_activate , name = 'user_activate'),
    ]