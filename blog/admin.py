from django.contrib import admin
from blog.models import Blog, Category, ImageDocument, DocDocument

class BlogAdmin(admin.ModelAdmin):
    #exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(ImageDocument)
admin.site.register(DocDocument)
