from django.contrib import admin

# Register your models here.
from .models import BlogCategory, BlogPost, BlogTag


class BlogPostAdmin(admin.ModelAdmin):
    pass


class BlogCategoryAdmin(admin.ModelAdmin):
    pass


class BlogTagAdmin(admin.ModelAdmin):
    pass


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogTag, BlogTagAdmin)
