from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Blog, Category

# Create your views here.

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:10:-1],
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
        'posts': Blog.objects.filter(category=category)[::-1]
    })

def view_about(request):
    return render_to_response('about.html',)
    
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('No search term was received')
            return render_to_response('blog/search_results.html', {
            'error': errors
            })
        elif len(q) > 100:
            errors.append('Search term must be less than 100 characters')
            return render_to_response('blog/search_results.html', {
            'error': errors
            })
            
        else:
            return render_to_response('blog/search_results.html',{
            'foundposts': Blog.objects.filter(body__icontains=q)[::-1], 
            'query': q
        })
    else:
        return render_to_response('blog/search_results.html', {
        'error': errors
    })
    