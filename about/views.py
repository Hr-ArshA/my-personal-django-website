from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

# Create your views here.
from about.models import About


class about_us(DetailView):
    queryset = About.objects.filter(slug='about')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context