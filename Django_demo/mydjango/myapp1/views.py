from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse

def index(request):
	return render(request, 'myapp1/index.html')

def url_reverse(request):
	# 进行反向解析
	print('反向解析结果：' + reverse('myapp1_url_reverse'))
	return render(request, '2/url_reverse.html')

def test_render(request):
	return render(request, 'myapp1/test_render.html', {'info':'myapp1'}, content_type='text/html')