from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
	path('myapp/index/', views.index),
    path('myapp/show/<int:id>/', views.show),
    path('myapp/test_get/', views.test_get),
    path('myapp/test_response', views.test_response),
    path('myapp/test_redirect_views/<int:id>/',views.test_redirect_views,name='app2_test_redirect_views'),
    path('myapp/test_redirect/',views.test_redirect,name='app2_test_redirect'),
]

