from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView, CreateView, DateDetailView
from django.utils.safestring import mark_safe
import markdown

from .models import ArticleTags, ArticleCategory, Articles
from .forms import ArticlesForm, ArticlesPagedownForm, ArticlesMarkdownXForm, ArticlesCkeditorForm

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
        # django-markdown-editor == martor 模板中用safe_markdown替代
        # from martor.settings import MARTOR_MARKDOWN_EXTENSIONS, MARTOR_MARKDOWN_SAFE_MODE, MARTOR_MARKDOWN_EXTENSION_CONFIGS
        # convert_obj = markdown.markdown(
        #     obj.content,
        #     safe_mode=MARTOR_MARKDOWN_SAFE_MODE,
        #     extensions=MARTOR_MARKDOWN_EXTENSIONS,
        #     extension_configs=MARTOR_MARKDOWN_EXTENSION_CONFIGS
        # )

        # md = markdown.Markdown(extensions=[
        #     'markdown.extensions.toc',
        # ], safe_mode=True, enable_attributes=False)
        # md.convert(obj.content)
        # obj.toc = md.toc
        # obj.content = mark_safe(convert_obj)
        return obj
    
    def get_context_data(self, **kwargs):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.toc',
        ], extension_configs={"toc": {
            "slugify": "markdown.extensions.headerid.slugify",
            "toc_depth": 1
        }})
        md.convert(self.object.content)
        toc = md.toc
        context = {"toc": toc}
        context.update(kwargs)
        return super(ArticlesDetailView, self).get_context_data(**context)
        

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

    def get_form_class(self):
        editor = self.request.GET.get("editor", '')
        if editor == "pagedown":
            return ArticlesPagedownForm
        elif editor == 'markdownx':
            return ArticlesMarkdownXForm
        elif editor == 'ckeditor':
            return ArticlesCkeditorForm
        return self.form_class
        # return super(ArticlesCreateView, self).get_form_class()


