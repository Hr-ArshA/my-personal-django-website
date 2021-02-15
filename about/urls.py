from django.urls import path
from about.views import about_us


urlpatterns = [
    path('a/<slug:slug>/', about_us.as_view(), name='about')
]