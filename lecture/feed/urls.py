#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from lecture.feed import views

urlpatterns = [
    url(r'^feedroot/$', views.FeedRootList.as_view()),
    url(r'^feedroot/(?P<feedroot_pk>[0-9]+)/$', views.FeedRootDetail.as_view()),
    url(r'^feedroot/(?P<feedroot_pk>[0-9]+)/(?P<feed_pk>[0-9]+)$', views.FeedDetail.as_view()),
]