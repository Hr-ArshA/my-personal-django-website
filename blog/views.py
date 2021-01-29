from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


# Create your views here.


class Blog(ListView):
    queryset = Post.objects.filter(Status=False)
    paginate_by = 8

class blog_detail(DetailView):
    queryset = Post.objects.filter(Status=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context