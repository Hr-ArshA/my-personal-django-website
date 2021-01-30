from django.shortcuts import render, get_object_or_404

from blog.models import Category, Post


def header(request, *args, **kwargs):
    context = {
        'category': Category.objects.filter(Status=True),
        'Post': Post.objects.filter(Status=True),
    }
    return render(request, 'blog/shared/header.html', context)

def footer(request, *args, **kwargs):
    context = {
        'category': Category.objects.filter(Status=True),
        'Post': Post.objects.filter(Status=True),
    }
    return render(request, 'blog/shared/footer.html', context)