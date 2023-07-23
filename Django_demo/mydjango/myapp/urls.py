from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
	path('myapp/index/', views.index),
    path('myapp/show/<int:id>/', views.show),
    path('myapp/test_get/', views.test_get)
]