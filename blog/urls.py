from django.urls import path

from blog.views import Blog, blog_detail, sidebar, category_list, Author_list

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('<slug:slug>/', blog_detail.as_view(), name='blog_detail'),
    path('sidebar', sidebar, name='sidebar'),
    path('category/<slug:slug>', category_list.as_view(), name='category'),
    path('author/<slug:username>', Author_list.as_view(), name='author'),
]
