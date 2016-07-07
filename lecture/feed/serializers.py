#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from lecture.feed.models import Feed, FeedRoot


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ('id', 'title', 'url')


class FeedRootSerializer(serializers.ModelSerializer):
    feeds = FeedSerializer(many=True)

    class Meta:
        model = FeedRoot
        fields = ('id', 'title', 'feeds')
