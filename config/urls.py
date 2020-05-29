
from django.contrib import admin
from django.urls import path, include
import page.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
]
