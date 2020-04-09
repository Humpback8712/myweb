from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'index.html')


def blog_index(request):

    return render(request, 'blog_index.html')
