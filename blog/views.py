from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    RedirectView,
)
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class PostLikeAPIToggle(APIView):
    authentication_classes = [authentication.SessionAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]
    # permission_classes = (permissions.AllowAny,)

    def get(self, request, pk, format=None):
        post = get_object_or_404(Post, id=self.request.GET.get('post_id'))
        url_ = post.get_absolute_url()
        updated = False
        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(self.request.user)
            liked = False
            updated = True
        else:
            post.likes.add(self.request.user)
            liked = True
            updated = True
        data = {
            'updated': updated,
            'liked': liked,
        }
        return Response(data)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        posts = Post.objects.all()
        liked_ids = []
        for post in posts:
            if post.likes.filter(id=self.request.user.id).exists():
                liked_ids.append(post.id)
        context['liked_ids'] = liked_ids
        return context

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user-posts.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        posts = Post.objects.all()
        liked_ids = []
        for post in posts:
            if post.likes.filter(id=self.request.user.id).exists():
                liked_ids.append(post.id)
        context['liked_ids'] = liked_ids
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'post_pic']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'post_pic']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
