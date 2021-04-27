from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import CommentForm
from .models import Post


class Home(ListView):
    model = Post
    template_name = 'blogpost.html'


class BlogView(DetailView):
    model = Post
    template_name = 'bogie.html'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['commentform'] = CommentForm()
        return context

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.author = self.request.user
            obj.save()
            return redirect('article-details', post.pk)

class BlogPost(CreateView):
    model = Post
    template_name = 'postblog.html'
    fields = '__all__'

