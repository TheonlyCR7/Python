from django.contrib import admin
from django.urls import path
from django.urls import re_path
from myapp2 import views

urlpatterns = [
    path('myapp2/index/', views.index),
    re_path(r'myapp2/list/(?P<year>\d{4})/', views.article_list),
    path('myapp2/test_redirect_model/<int:id>/',views.test_redirect_model,name='myapp2_test_redirect_model'),
    path('myapp2/userinfo/<int:id>/',views.userinfo,name='myapp2_userinfo'),
]
