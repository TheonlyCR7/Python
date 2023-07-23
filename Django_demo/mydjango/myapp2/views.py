from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'myapp2/index.html')

def article_list(request, year):
	return HttpResponse("myapp2中的article方法, 参数为year, 指定4位, 值为" + str(year))
