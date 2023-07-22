from django.contrib import admin
from django.urls import path
from myapp2 import views

urlpatterns = [
    path('myapp2/index/', views.index),
]
