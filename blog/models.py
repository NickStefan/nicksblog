from django.db import models
from django.db.models import permalink

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    @permalink # this puts a 'view on site' link in the admin
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})
        
    def __unicode__(self):
        return '%s' % self.title
        
class Blog (models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True) #auto_now_add=True
    category = models.ManyToManyField(Category)
    live = models.BooleanField(default=False)
    
    def __unicode__(self):
        return '%s' % self.title
    
    @permalink # this puts a 'view on site' link in the admin
    def get_absolute_url(self):
        if self.live == True:
            return ('view_blog_post', None, {'slug': self.slug})
        else:
            return ('view_blog_preview', None, {'slug': self.slug})
        
