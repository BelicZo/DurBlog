from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base/$', TemplateView.as_view(template_name='base/base.html')),
    url(r'^$', TemplateView.as_view(template_name='list.html')),
    url(r'^list/$', TemplateView.as_view(template_name='list.html'), name='list'),
    url(r'^show/$', TemplateView.as_view(template_name='show.html'), name='show'),

]

from articles import views
from articles.urls import articles_patterns
urlpatterns += [
    # url('^blog/$', views.ArticlesListView.as_view(), name="blog_list"),
    # url('^blog/(?P<pk>[0-9]{1,3})/$', views.ArticlesDetailView.as_view(), name='blog_detail'),
    # url('^', include("articles.urls", namespace='blog')),
    url('^', include(articles_patterns)),
    # url('^new_blog/$', views.ArticlesCreateView.as_view(), name="blog_create"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^martor/', include('martor.urls')),
]
