"""
URL configuration for mydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp2 import views as v2
from myapp import views as v1
from mydjango import views as v

urlpatterns = [
    path('', v.index),
    path('admin/', admin.site.urls),
    path('index/', v1.index, name='index'),
    path('', include('myapp.urls')),
    path('', include('myapp1.urls')),
    path('', include('myapp2.urls')),
    path('', include('myapp3.urls')),
]