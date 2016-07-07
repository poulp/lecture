from django.contrib import admin

from lecture.feed.models import Feed, FeedRoot

admin.site.register(Feed)
admin.site.register(FeedRoot)