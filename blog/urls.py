from django.urls import path

from blog.views import Blog, blog_detail

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('/<slug:slug>/', blog_detail.as_view(), name='blog_detail')
]