from django.conf.urls import patterns, include, url
from settings import *
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nickswebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'blog.views.index'),
    
    url(r'^blog/view/(?P<slug>[^\.]+)',
    'blog.views.view_post',
    name='view_blog_post'),
    
    url(r'^blog/category/(?P<slug>[^\.]+)',
    'blog.views.view_category',
    name='view_blog_category'),
    url(r'^about/', 'blog.views.view_about'),
    url(r'^admin/', include(admin.site.urls)),
)
