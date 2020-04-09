from django.contrib import admin
from django.urls import path, include
from .views import index, blog_index

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('blog_index', blog_index, name='blog_index')
]
