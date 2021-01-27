from django.urls import path

from .views import loginUser, register

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('register/', register, name='register'),
]