from django.shortcuts import render
from .models import Post, CreatePost
from django.views.generic import CreateView


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'blog/post_list.html')
    return render(request, 'blog/create_blog.html')


def add_post(request):
    # Logic for adding a post
    return render(request, 'blog/add_post.html')