from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab1_home, name='lab1_home'),
    path('about/', views.lab1_about, name='lab1_about'),
    path('gallery/', views.lab1_gallery, name='lab1_gallery'),
]