from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Blog, Category, Document
from blog.forms import DocumentForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.distinct().filter(blog__live=True),
        'posts': Blog.objects.filter(live=True)[:100:-1],
    })

def view_post(request, slug):
    return render_to_response('blog/view_post.html',{
        'post': get_object_or_404(Blog, slug=slug)
    })

@staff_member_required
def preview_post(request, slug):
    return render_to_response('blog/view_post.html',{
        'post': get_object_or_404(Blog, slug=slug)
    })

@staff_member_required
def list(request):
    #handle file upload
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():

            if request.FILES.get('docfile'):
              newdoc = Document(docfile = request.FILES['docfile'])
              newdoc.save()

            if request.FILES.get('imgfile'):
              newimg = Document(imgfile = request.FILES['imgfile'])
              newimg.save()

            if request.FILES.get('jsfile'):
              newjs = Document(jsfile = request.FILES['jsfile'])
              newjs.save()

            form = DocumentForm() #empty unbound form
            documents = Document.objects.all()
            return render_to_response('blog/list.html', {
                'documents': documents, 'form': form
                }, context_instance=RequestContext(request))
    else:
        form = DocumentForm() #empty unbound form
        documents = Document.objects.all()
        return render_to_response('blog/list.html', {
            'documents': documents, 'form': form
            }, context_instance=RequestContext(request))


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html',{
        'category': get_object_or_404(Category, slug=slug),
        'posts': Blog.objects.filter(category=category,live=True).order_by('-posted')
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
            'foundposts': Blog.objects.filter(live=True).filter(body__icontains=q)[::-1],
            'query': q
        })
    else:
        return render_to_response('blog/search_results.html', {
        'error': errors
    })
