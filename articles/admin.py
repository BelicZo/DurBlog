from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from markdownx.widgets import MarkdownxWidget
from martor.widgets import AdminMartorWidget
# Register your models here.
from .models import ArticleCategory, Articles, ArticleTags


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': CKEditorWidget()}}


class ArticleCategoryAdmin(admin.ModelAdmin):
    pass


class ArticleTagsAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Articles, ArticlesAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(ArticleTags, ArticleTagsAdmin)
