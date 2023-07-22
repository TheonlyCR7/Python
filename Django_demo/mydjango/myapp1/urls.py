from django.contrib import admin
from django.urls import path
from myapp1 import views

urlpatterns = [
    path('myapp1/index/', views.index),
]