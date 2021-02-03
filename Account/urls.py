from django.urls import path

from .views import loginUser, register

urlpatterns = [
    path('h/login/', loginUser, name='login'),
    path('h/register/', register, name='register'),
]