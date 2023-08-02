from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView # 导入类

class TestTemplateView(TemplateView): # 继承类
    # 设置模板文件
    template_name="myapp3/test_templateview.html"
    
    # 重写父类get_context_data()方法
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        #增加模板变量info
        context["info"]="该变量可以传递到模板" # 可以在模板中得到传递的字典变量
        return context
    

# 先导入
from django.views.generic import ListView
from .models import *


class TestListView(ListView):
    model=UserBaseInfo
    template_name="myapp3/test_listview.html"
    #设置模板变量
    #context_object_name="users"
    #每页显示的条数
    paginate_by=1

    #queryset=UserBaseInfo.objects.filter(status=1)
    #重新父类的get_queryset()
    def get_queryset(self):
        #返回状态为1的数据
        userinfo=UserBaseInfo.objects.all()
        return userinfo
    
    #重写父类get_context_data()方法
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        #增加模板变量info
        context["info"]="ListView变量可以传递到模板"
        print(context)
        return context