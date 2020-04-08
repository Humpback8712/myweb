
from django.contrib import admin
from django.urls import path, include
from app import urls as appurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(appurls))
]
