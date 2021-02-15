from Account.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from blog.models import Post, Category
from django.db.models import Q


# Create your views here.

def sidebar(request, *args, **kwargs):
    context = {
        'category': Category.objects.filter(Status=True),
        'Post': Post.objects.filter(Status=True)[:3],
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

class category_list(ListView):
    template_name = 'blog/category.html'
    paginate_by = 8

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.posts.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category

        return context

class Author_list(ListView):
    template_name = 'blog/Author.html'
    paginate_by = 8

    def get_queryset(self):
        global Author
        username = self.kwargs.get('username')
        Author = get_object_or_404(User, username=username)
        return Author.posts.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Author'] = Author

        return context


class Serach_list(ListView):
    template_name = 'blog/search.html'
    paginate_by = 8

    def get_queryset(self):
        search = self.request.GET.get('q')
        return Post.objects.filter(Q(Description__icontains=search) | Q(Title__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')

        return context