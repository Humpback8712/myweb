from django.contrib import admin
from django.urls import path, include
from .views import index, blog_index, blog_list, blog_content

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('blog_index', blog_index, name='blog_index'),
    path('blog_list/<str:catalogue>', blog_list, name='blog_list'),
    path('blog_list/blog_content/<int:num>', blog_content, name='blog_content'),

]
