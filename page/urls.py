from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/<int:profile_id>/', views.detail, name="detail"),
    path('introduce/', views.introduce, name="introduce"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
]