from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
import markdown

from .models import BlogTag, BlogCategory, BlogPost


class BlogPostDetailView(DetailView):
    queryset = BlogPost.objects.all()
    template_name = 'article.html'
    context_object_name = 'blog_post'

    def get_object(self, queryset=None):
        obj = super(BlogPostDetailView, self).get_object(self.queryset)
        # obj.content = markdown.markdown(obj.content, extensions=[
        #     'markdown.extensions.fenced_code',
        #     'markdown.extensions.extra',
        #     'markdown.extensions.codehilite',
        #     'markdown.extensions.table',
        #     'markdown.extensions.toc'], safe_mode=True, enable_attributes=False)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ], safe_mode=True, enable_attributes=False)
        obj.content = md.convert(obj.content)
        obj.toc = md.toc
        return obj


class BlogPostListView(ListView):
    queryset = BlogPost.objects.all()
    context_object_name = 'blog_posts'
    template_name = 'list.html'

