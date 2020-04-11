from django.db import models
import django.utils.timezone as timezone


class TagInfo(models.Model):

    tag_name = models.CharField(max_length=20)

    def __str__(self):

        return self.tag_name


class BlogInfo(models.Model):

    blog_title = models.CharField(max_length=20)
    blog_content = models.TextField()
    blog_summary = models.CharField(max_length=100)
    add_date = models.DateTimeField('保存日期', default=timezone.now)
    catalogue = models.CharField(max_length=30)
    tag = models.ForeignKey(TagInfo, on_delete=models.CASCADE)

    def __str__(self):

        return self.blog_title
