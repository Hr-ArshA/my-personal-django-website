from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from blog.models import Post, Category


# Create your views here.

def sidebar(request, *args, **kwargs):
    context = {
        'category': Category.objects.filter(Status=True),
        'Post': Post.objects.filter(Status=True),
    }
    return render(request, 'blog/sidebar.html', context)


class Blog(ListView):
    queryset = Post.objects.filter(Status=True)
    paginate_by = 8

class blog_detail(DetailView):
    queryset = Post.objects.filter(Status=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context



