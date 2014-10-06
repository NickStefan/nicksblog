from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Blog, Category, ImageDocument, DocDocument
from blog.forms import ImageDocumentForm, DocDocumentForm
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext

# Create your views here.

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.distinct().filter(blog__live=True),
        'posts': Blog.objects.filter(live=True)[:30:-1],
    })

def view_post(request, slug):
    return render_to_response('blog/view_post.html',{
        'post': get_object_or_404(Blog, slug=slug)
    },context_instance=RequestContext(request))

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html',{
        'category': get_object_or_404(Category, slug=slug),
        'posts': Blog.objects.filter(category=category,live=True).order_by('-posted')
    })

def view_about(request):
    return render_to_response('about.html',)

@staff_member_required
def preview_post(request, slug):
    return render_to_response('blog/view_post.html',{
        'post': get_object_or_404(Blog, slug=slug)
    })

@staff_member_required
def upload_image(request):
    #handle file upload
    if request.method == "POST":
        print "posted"
        form = ImageDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print "valid"

            if request.FILES.get('imgfile'):
              newimg = ImageDocument(imgfile = request.FILES['imgfile'])
              newimg.save()
              print "saved"

            form = ImageDocumentForm() #empty unbound form
            documents = ImageDocument.objects.all()

            return render_to_response('blog/imagelist.html', {
                'documents': documents, 'form': form
                }, context_instance=RequestContext(request))
        else:
            print "not valid"
            form = ImageDocumentForm() #empty unbound form
            documents = ImageDocument.objects.all()
            return render_to_response('blog/imagelist.html', {
                'documents': documents, 'form': form
                }, context_instance=RequestContext(request))
    else:
        "print nope"
        form = ImageDocumentForm() #empty unbound form
        documents = ImageDocument.objects.all()
        return render_to_response('blog/imagelist.html', {
            'documents': documents, 'form': form
            }, context_instance=RequestContext(request))

@staff_member_required
def upload_doc(request):
    #handle file upload
    if request.method == "POST":
        form = DocDocumentForm(request.POST, request.FILES)
        if form.is_valid():

            if request.FILES.get('docfile'):
              newdoc = DocDocument(docfile = request.FILES['docfile'])
              newdoc.save()

            form = DocDocumentForm() #empty unbound form
            documents = DocDocument.objects.all()

            return render_to_response('blog/doclist.html', {
                'documents': documents, 'form': form
                }, context_instance=RequestContext(request))
        else:
            form = DocDocumentForm() #empty unbound form
            documents = DocDocument.objects.all()
            return render_to_response('blog/doclist.html', {
                'documents': documents, 'form': form
                }, context_instance=RequestContext(request))
    else:
        form = DocDocumentForm() #empty unbound form
        documents = DocDocument.objects.all()
        return render_to_response('blog/doclist.html', {
            'documents': documents, 'form': form
            }, context_instance=RequestContext(request))


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
