from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


# Create your views here.


class Blog(ListView):
    queryset = Post.objects.all()
    paginate_by = 8
