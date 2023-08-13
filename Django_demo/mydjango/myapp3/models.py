from django.db import models
from django.urls import reverse

class UserBaseInfo(models.Model):
    id=models.AutoField(verbose_name='编号',primary_key=True)
    username = models.CharField(verbose_name='用户名称',max_length=30)
    password = models.CharField(verbose_name='密码',max_length=20)
    status = models.CharField(verbose_name='状态',max_length=1)
    createdate = models.DateTimeField(verbose_name='创建日期',db_column='createDate')

    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse('myapp3_userinfo',kwargs={'id':self.pk})

    class Meta:
        verbose_name='人员基本信息'
        db_table = 'UserBaseInfo3'


from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView # 导入类

class TestTemplateView(TemplateView): # 继承类
    # 设置模板文件
    template_name="2/test_templateview.html"
    
    # 重写父类get_context_data()方法
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        #增加模板变量info
        context["info"]="该变量可以传递到模板" # 可以在模板中得到传递的字典变量
        return context


