#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class FeedRoot(models.Model):

    class Meta(object):
        verbose_name = 'FeedRoot'
        verbose_name_plural = 'FeedRoots'

    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Feed(models.Model):

    class Meta(object):
        verbose_name = 'Feed'
        verbose_name_plural = 'Feeds'

    title = models.CharField('Label', max_length=200)
    url = models.URLField('Feed')
    root = models.ForeignKey(FeedRoot, related_name='feeds')

    def __str__(self):
        return self.title
