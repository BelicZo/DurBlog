from django.dispatch import Signal, receiver
from django.db.models.signals import pre_save

from .models import Articles


@receiver(pre_save, sender=Articles)
def validator_articles(sender, instance=None, **kwargs):

    print("Save Articles", __name__, __file__)
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist as e:
        print("这是一个新的数据")
        print(e)
        instance.slug = instance.generate_unique_slug()
    else:
        print(f"old instance title: {old_instance.title}")
        if instance.title != old_instance.title or not old_instance.slug:
            instance.slug = instance.generate_unique_slug()
    print(f"new instance title: {instance.title}")
    print(sender, kwargs)
    # instance.full_clean()
    # Save Articles articles.signals C:\Users\Belick\Desktop\Stu\MyProject\Blog-django\DurBlog\articles\signals.py
    # <class 'articles.models.Articles'> {'signal': <django.db.models.signals.ModelSignal object at 0x000001DF44EE7DD8>,
    # 'instance': 1--SQL语句--2018-07-26 22:22:37.685433, 'raw': False, 'using': 'default', 'update_fields': None}

