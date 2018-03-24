from django.db import models


# Create your models here.


class BlogCategory(models.Model):
    name = models.CharField("分类名", unique=True, max_length=100, db_index=True)
    index = models.SmallIntegerField("排序", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = verbose_name


class BlogTag(models.Model):
    name = models.CharField("标签名", db_index=True, max_length=100)
    index = models.SmallIntegerField("排序", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客标签"
        verbose_name_plural = verbose_name


class BlogPost(models.Model):
    title = models.CharField("标题", max_length=200, unique=True)
    content = models.TextField("内容")
    words_count = models.IntegerField(verbose_name="字数", default=0)
    allow_comment = models.BooleanField("允许评论", default=True)
    vote_count = models.IntegerField("点赞数", default=0)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="博文种类",
                                 related_name="category_posts")
    tags = models.ManyToManyField(BlogTag, related_name="tags_posts")
    published_at = models.DateTimeField("发表时间", blank=True, null=True, db_index=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        verbose_name = "博文"
        verbose_name_plural = verbose_name

    def __repr__(self):
        return "{} - {} - {}".format(self.pk, self.title, self.published_at)

    def __str__(self):
        return "{} - {} - {}".format(self.pk, self.title, self.published_at)
