from django.conf.urls import patterns, include, url
from django.conf import settings
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

    url(r'^blog/preview/(?P<slug>[^\.]+)',
    'blog.views.preview_post',
    name='view_blog_preview'),

    url(r'^blog/category/(?P<slug>[^\.]+)',
    'blog.views.view_category',
    name='view_blog_category'),
    url(r'^about/', 'blog.views.view_about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/search/$', 'blog.views.search'),
    url(r'^upload/img$','blog.views.upload_image'),
    url(r'^upload/doc$','blog.views.upload_doc'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media'})

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
