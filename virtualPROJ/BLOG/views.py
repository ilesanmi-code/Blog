from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class Home(ListView):
    model = Post
    template_name = 'blogpost.html'


class BlogView(DetailView):
    model = Post
    template_name = 'blogview.html'


class BlogPost(CreateView):
    model = Post
    template_name = 'postblog.html'
    fields = '__all__'
