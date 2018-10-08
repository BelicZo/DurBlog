from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView, CreateView, DateDetailView
from django.utils.safestring import mark_safe
import markdown

from .models import ArticleTags, ArticleCategory, Articles
from .forms import ArticlesForm

__all__ = ['ArticlesCreateView', 'ArticlesDetailView', 'ArticlesListView']


class ArticlesDetailView(DateDetailView):
    queryset = Articles.objects.all()
    template_name = 'article.html'
    context_object_name = 'blog_post'
    date_field = "updated_at"
    month_format = "%m"

    def get_object(self, queryset=None):
        obj = super(ArticlesDetailView, self).get_object(self.queryset)
        # obj.content = markdown.markdown(obj.content, extensions=[
        #     'markdown.extensions.fenced_code',
        #     'markdown.extensions.extra',
        #     'markdown.extensions.codehilite',
        #     'markdown.extensions.table',
        #     'markdown.extensions.toc'], safe_mode=True, enable_attributes=False)
        from martor.settings import MARTOR_MARKDOWN_EXTENSIONS, MARTOR_MARKDOWN_SAFE_MODE, MARTOR_MARKDOWN_EXTENSION_CONFIGS
        convert_obj = markdown.markdown(
            obj.content,
            safe_mode=MARTOR_MARKDOWN_SAFE_MODE,
            extensions=MARTOR_MARKDOWN_EXTENSIONS+['markdown.extensions.codehilite', 'markdown.extensions.tables',
                                                   'markdown.extensions.toc'],
            extension_configs=MARTOR_MARKDOWN_EXTENSION_CONFIGS
        )

        # md = markdown.Markdown(extensions=[
        #     'markdown.extensions.extra',
        #     'markdown.extensions.codehilite',
        #     'markdown.extensions.toc',
        # ], safe_mode=True, enable_attributes=False)
        # obj.content = md.convert(obj.content)
        # obj.toc = md.toc
        obj.content = mark_safe(convert_obj)
        return obj


class ArticlesListView(ListView):
    queryset = Articles.objects.all()
    context_object_name = 'blog_posts'
    template_name = 'list.html'


class ArticlesCreateView(CreateView):
    """"""
    template_name = 'writing.html'
    form_class = ArticlesForm
    model = Articles

    def form_invalid(self, form):
        return super(ArticlesCreateView, self).form_invalid(form)



