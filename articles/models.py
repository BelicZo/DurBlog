# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from martor.models import MartorField

# Create your models here.


class ArticleCategory(models.Model):
    name = models.CharField("分类名", unique=True, max_length=100, db_index=True)
    index = models.SmallIntegerField("排序", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = verbose_name


class ArticleTags(models.Model):
    name = models.CharField("标签名", db_index=True, max_length=100)
    index = models.SmallIntegerField("排序", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客标签"
        verbose_name_plural = verbose_name


class Articles(models.Model):
    DRAFT = 'D'  # 'Draft'
    PUBLISHED = 'P'  # 'Published'
    STATUS = (
        (DRAFT, '草稿'),
        (PUBLISHED, '发布'),
    )
    title = models.CharField("标题", max_length=200, unique=True)
    content = MartorField("内容")
    words_count = models.IntegerField(verbose_name="字数", default=0)
    allow_comment = models.BooleanField("允许评论", default=True)
    vote_count = models.IntegerField("点赞数", default=0)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="博文种类",
                                 related_name="article")
    tags = models.ManyToManyField(ArticleTags, related_name="article")
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    published_at = models.DateTimeField("发表时间", blank=True, null=True, db_index=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)
    pv = models.IntegerField(_("Page Views"), default=0)
    uv = models.IntegerField(_("User Views"), default=0)

    class Meta:
        verbose_name = "博文"
        verbose_name_plural = verbose_name

    def __repr__(self):
        return "{} - {} - {}".format(self.pk, self.title, self.published_at)

    def __str__(self):
        return "{} - {} - {}".format(self.pk, self.title, self.published_at)


class ArticleComment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
