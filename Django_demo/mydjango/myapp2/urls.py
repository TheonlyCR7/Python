from django.contrib import admin
from django.urls import path
from django.urls import re_path
from myapp2 import views

urlpatterns = [
    path('myapp2/index/', views.index),
    re_path(r'myapp2/list/(?P<year>\d{4})/', views.article_list),
]
