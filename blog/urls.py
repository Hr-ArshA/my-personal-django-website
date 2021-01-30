from django.urls import path

from blog.views import Blog, blog_detail, sidebar

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('<slug:slug>/', blog_detail.as_view(), name='blog_detail'),
    path('sidebar', sidebar, name='sidebar'),
    path('category/<slug:slug>', category_list.as_view(), name='category'),
]
