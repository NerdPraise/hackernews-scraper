from django.db import models
from django.db.models.base import Model
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

# Create your models here.


class News(models.Model):
    item_id = models.PositiveIntegerField(null=True)
    type = models.CharField(_('Item Type'), max_length=255)
    author = models.CharField(_('Item Author'), max_length=255)
    date_created = models.DateTimeField(_('Creation Time'), null=True)
    deleted = models.BooleanField(_('Is Item Deleted?'), default=False)
    dead = models.BooleanField(_('Is Item Dead?'), default=False)
    is_posted = models.BooleanField(_('Is Item Posted?'), default=False)
    kids = ArrayField(ArrayField(models.IntegerField()), blank=True, null=True)
    descendants = models.IntegerField(
        _('Comment count'), blank=True, null=True)
    score = models.IntegerField(_('Item Score'), blank=True, null=True)
    url = models.CharField(_('Item url'), max_length=255,null=True, blank=True)
    title = models.CharField(_('Item Title'), blank=True, max_length=255)

    def __str__(self):
        return str(self.id)



class Comment(models.Model):
    news = models.ForeignKey(
        'news_scrape.News', on_delete=models.CASCADE,
        verbose_name=_('base news'))
    parent = models.IntegerField(_('Comment Parent'), blank=True, null=True)
    text = models.TextField(_('Item Text'), max_length=255, blank=True)