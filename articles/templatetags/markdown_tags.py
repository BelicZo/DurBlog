# -*- coding: utf-8 -*-
# __author__ = "belic"
# __datetime__ = "2018/4/19 20:26"

import markdown
from django.utils.safestring import mark_safe
from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter()
# @stringfilter
def custom_markdown(value):
    return mark_safe(markdown.markdown(
           value,
           extensions=['markdown.extensions.fenced_code',   # 解析代码块
                       'markdown.extensions.codehilite',    # codehilite即为代码高亮准备
                       'markdown.extensions.table',    # 解析表格
                       'markdown.extensions.toc',    # 解析目录TOC

],
           safe_mode=True,
           enable_attributes=False))