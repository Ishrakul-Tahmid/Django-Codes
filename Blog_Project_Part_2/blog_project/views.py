from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home(request, category_slag = None):
    data = Post.objects.all()
    if category_slag is not None:
        category = Category.objects.get(slug = category_slag)
        data = Post.objects.filter(category = category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'data': data, 'category': categories})