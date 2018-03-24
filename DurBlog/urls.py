"""MyFirstBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base/$', TemplateView.as_view(template_name='_base.html')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^list/$', TemplateView.as_view(template_name='list.html'), name='list'),
    url(r'^show/$', TemplateView.as_view(template_name='show.html'), name='show'),
]

from articles.views import *

urlpatterns += [
    url('^blog/$', BlogPostListView.as_view(), name="blog_list"),
    url('^blog/(?P<pk>[0-9]{1,3})/$', BlogPostDetailView.as_view(), name='blog_detail'),
]
