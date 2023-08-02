from django.urls import path
from myapp3.views_class import *

# 路径里面添加
urlpatterns = [
    path('myapp3/test_templateview', TestTemplateView.as_view()),
]
