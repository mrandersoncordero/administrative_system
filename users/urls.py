"""Users URLs."""

# Django
from django.urls import path

# Views
from . import views

app_name = 'users'
urlpatterns = [
    path('sign-in', views.sign_in, name='sign-in'),
]