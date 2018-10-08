# coding: utf-8
from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    name = 'articles'
    verbose_name = '博文'

    def ready(self):
        from . import signals
        super(ArticlesConfig, self).ready()
