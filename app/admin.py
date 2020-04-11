from django.contrib import admin
from . import models


class BlogInfoadmin(admin.ModelAdmin):
    list_display = ['id', 'blog_title', 'blog_summary', 'add_date', 'tag']


class TagInfoadmin(admin.ModelAdmin):
    list_display = ['tag_name']


admin.site.register(models.BlogInfo)
admin.site.register(models.TagInfo)
