from django.contrib import admin
from django.urls import path
from myapp1 import views

urlpatterns = [
    path('myapp1/index/', views.index),
    path('myapp1/url_reverse/', views.url_reverse, name = 'myapp1_url_reverse'),
    path('myapp1/test_render', views.test_render)
]