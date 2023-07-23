from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return render("request, 'myapp/index.html'")

def show(request, id):
	return HttpResponse('myapp中的show方法, 参数为id, 值为' + str(id))

def test_get(request):
	print(request.get_host())
	# print(request.get_raw_uri())
	print(request.path)
	print(request.get_full_path())
	print(request.method)
	print(request.GET)
	# print(request.META['RAW_URI']) 
	print(request.build_absolute_uri())
	print(request.META['HTTP_USER_AGENT'])
	print(request.META['REMOTE_ADDR'])
	print(request.GET.get('username'))
	return HttpResponse('')

