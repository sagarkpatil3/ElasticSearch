# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify

from django.db import models
from .search import PostIndex

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=200)
    number = models.IntegerField()

    slug = models.SlugField(default='', blank=True)

    def indexing(self):
        obj = PostIndex(
            meta={'id': self.id},
            text=self.text,
            number = self.number,
        )
        obj.save()
        return obj.to_dict(include_meta=True)

    def save(self):
        self.slug = slugify(self.text)
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.text

