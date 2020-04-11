from django.shortcuts import render
from app.models import BlogInfo
import markdown
# Create your views here.


def index(request):

    return render(request, 'index.html')


def blog_index(request):

    return render(request, 'blog_index.html')


def blog_list(request, catalogue):

    blogs = BlogInfo.objects.filter(catalogue=catalogue)

    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_content(request, num):

    blog = BlogInfo.objects.get(id=num)
    blog.blog_content = markdown.markdown(blog.blog_content, extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    return render(request, 'blog_content.html', {'blog': blog})



