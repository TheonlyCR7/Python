from django.urls import path
from myapp3.views_class import *

# 路径里面添加
urlpatterns = [
    path('myapp3/test_templateview', TestTemplateView.as_view()),
    path('myapp3/test_listview/',TestListView.as_view()),
    path('myapp3/test_detailview/<int:pk>', TestDetailView.as_view(), name = 'test-detail'),
]
