# -*- coding: utf-8 -*-
# __author__ = "belic"
# __datetime__ = "2018/7/25 21:36"
from django import forms
from pagedown.widgets import PagedownWidget
from markdownx.fields import MarkdownxFormField, MarkdownxWidget
from martor.models import MartorFormField
from martor.widgets import MartorWidget
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField

from .models import Articles


class ArticlesBaseForm(forms.ModelForm):

    class Meta:
        abstract = True
        model = Articles
        fields = ("title", "content", "allow_comment", "status", "category", "tags")


class ArticlesForm(ArticlesBaseForm):
    """"""
    # content = forms.CharField(widget=PagedownWidget())
    content = MartorFormField()


class ArticlesPagedownForm1(ArticlesBaseForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=True))


ArticlesPagedownForm = type('', (ArticlesBaseForm,), {'content': forms.CharField(widget=PagedownWidget(show_preview=True))})

ArticlesMarkdownXForm = type('', (ArticlesBaseForm,), {'content': MarkdownxFormField()})

ArticlesCkeditorForm = type('', (ArticlesBaseForm,), {'content': RichTextUploadingFormField()})


