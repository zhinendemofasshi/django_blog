from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Category, Post
# they are logics of the blog application


def index(request):
    """logics of homepage of the website"""
    # get all categories and posts
    category_list = Category.objects.all()
    post_list = Post.objects.all()
    context = {'category_list': category_list, 'post_list': post_list}
    # pass data to the frontend
    return render(request, 'blog/index.html', context)


def category_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # get all the posts of a category
    posts = category.post_set.all()
    context = {'category': category, 'post_list': posts}
    return render(request, 'blog/list.html', context)


def post_detail(request, post_id):
    """this view can show content of a post"""
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)