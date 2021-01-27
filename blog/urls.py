from django.urls import path

from blog.views import Blog

urlpatterns = [
    path('', Blog.as_view(), name='blog')
]