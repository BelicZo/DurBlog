from django.urls import re_path, path, include

from .views import *

# app_name = 'articles'
articles_patterns = ([
    re_path('^new_blog/$', ArticlesCreateView.as_view(), name="blog_create"),
    re_path("^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>.*)/$",
            ArticlesDetailView.as_view(), name="blog_detail")
], 'articles')

