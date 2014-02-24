from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Blog, Category

# Create your views here.

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:10:-1]
    })

def view_post(request, slug):
    return render_to_response('blog/view_post.html',{
        #'categories': Category.objects.filter(title=title),
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html',{
        'category': get_object_or_404(Category, slug=slug),
        'posts': Blog.objects.filter(category=category)[:5]
    })

def view_about(request):
    return render_to_response('about.html',)