# -*- coding: utf-8 -*-
# __author__ = "belic"
# __datetime__ = "2018/7/25 21:36"
from django import forms
from pagedown.widgets import PagedownWidget
# from markdownx.fields import MarkdownxFormField, MarkdownxWidget
from martor.models import MartorFormField
from martor.widgets import MartorWidget

from .models import Articles


class ArticlesForm(forms.ModelForm):
    """"""
    # content = forms.CharField(widget=PagedownWidget())
    content = MartorFormField()

    class Meta:
        model = Articles
        fields = ("title", "content", "allow_comment", "status", "category", "tags")
