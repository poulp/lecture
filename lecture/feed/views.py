#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from lecture.feed.models import Feed, FeedRoot
from lecture.feed.serializers import FeedSerializer, FeedRootSerializer


class FeedRootList(generics.ListCreateAPIView):
    serializer_class = FeedRootSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return FeedRoot.objects.filter(owner=self.request.user)


class FeedRootDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedRoot.objects.all()
    serializer_class = FeedRootSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'feedroot_pk'


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'feed_pk'

