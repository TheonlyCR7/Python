# 1. 视图函数

用于处理客户端的请求并生成响应数据。在views使用函数处理请求的方式，被称为视图函数，也叫作FBV(Function Base Views). 

一个简单的视图函数：在views.py里面配置

```python
from django.http import HttpResponse  # 导入HttpResponse类

def index(request):  # 接收HttpRequest请求对象
	return HttpResponse('Hello Django!')  # 返回一个HttpResponse对象，包含响应数据
```



## 1.1 视图函数的底层原理

* 主要使用 `HttpRequest` 请求对象和 `HttpResponse` 响应对象。
* 当浏览器向服务器发送请求，Django先创建一个HttpRequest对象。
* 然后加载对应视图，将这个HttpRequest对象作为第1个参数传递给视图函数。
* 视图函数处理后返回一个 `HttpResponse` 对象

## 1.2 `HttpRequest`对象

### 包含的属性

| 属性         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| body         | 获取请求体的内容。如果请求不包含主体，则返回空字节串。如果内容已经被读取过，则再次访问会返回空字节串。 |
| content_type | 获取请求体的 MIME 类型，例如 "text/plain" 或 "application/json"。 |
| GET          | 获取 GET 请求参数。这是一个类似于字典的对象，可以使用 get() 方法获取其值。例如，如果请求的 URL 中包含如下查询字符串 ?foo=bar，则可以通过 request.GET["foo"] 获取到 "bar"。 |
| POST         | 获取 POST 请求参数。这是一个类似于字典的对象，可以使用 get() 方法获取其值。如果请求没有数据，则返回一个空的 QueryDict 对象。 |
| FILES        | 获取上传的文件。这是一个类似于字典的对象，其中包含上传的每个文件，每个文件都是一个 UploadedFile 对象。 |
| META         | 获取请求的元数据，这是一个包含所有 HTTP 头的字典。例如，request.META['HTTP_USER_AGENT'] 将返回浏览器的 User-Agent。 |
| COOKIES      | 获取请求携带的 cookie。这是一个包含所有 cookie 值的字典。    |
| method       | 获取请求方法。例如，GET、POST 或 PUT。                       |
| path         | 获取请求路径。例如，"/my_path/"。                            |
| scheme       | 获取请求协议。例如，"http" 或 "https"。                      |

### 包含的方法

| 方法                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| is_ajax()                                                    | 判断请求是否为 ajax 请求。如果请求包含名为 HTTP_X_REQUESTED_WITH 的头，且值为 XMLHttpRequest，则返回 True，否则返回 False。 |
| is_secure()                                                  | 判断请求是否是通过安全连接的 HTTPS 处理。如果请求是通过 HTTPS 处理，则返回 True，否则返回 False。 |
| is_mulitpart()                                               | 判断请求是否是multipart/form-data类型。如果请求是multipart/form-data类型，则返回 True，否则返回 False。 |
| is_empty()                                                   | 判断参数是否为空。如果参数为空，则返回 True，否则返回 False。 |
| is_multivalued()                                             | 判断参数是否支持多值。如果参数支持多值（即为类似于 foo=1&foo=2 的查询字符串语法），则返回 True，否则返回 False。 |
| QueryDict()                                                  | 将查询字符串或请求体转换为一个字典。query_string 参数是字符串，将作为查询字符串或请求体进行解析。mutable 参数指定返回的 QueryDict 是否可变。encoding 参数指定解码查询字符串或请求体的编码。如果 encoding 没有指定，则使用 settings.DEFAULT_CHARSET。QueryDict 对象是类似于字典的对象，可以使用 get() 方法获取其值。 |
| build_absolute_uri(location=None)                            | 构建绝对 URL。location 参数指定目标 URL 的路径部分，如果省略，则使用请求的路径。 |
| get_host()                                                   | 获取请求的主机名。如果请求使用主机名（即存在 HOST 头），则返回该主机名。否则，返回内置的默认主机名。 |
| get_port()                                                   | 获取请求的端口号。如果请求使用常规端口（即端口是 80 或 443），则返回 None。否则，返回请求使用的端口号。 |
| get_full_path()                                              | 获取请求的完整路径，包括查询字符串。例如，"/my_path/?foo=bar"。 |
| get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None) | 获取已签名的 cookie。key 参数指定要获取的 cookie 的名称。default 参数指定如果 cookie 不存在要返回的默认值。salt 参数是在计算签名时使用的加盐值。max_age 参数指定 cookie 的最大寿命（秒数）。如果 cookie 没有签名或签名无效，则会引发 django.core.signing.BadSignature 异常。 |
| headers                                                      | 获取请求头。这是一个包含所有 HTTP 头的字典。                 |
| user                                                         | 获取当前用户。如果用户未经过身份验证，则将返回 AnonymousUser 的实例。 |
| session                                                      | 获取当前会话。如果会话不存在，则会引发 AttributeError 异常。 |



### 主要的属性和方法

| 属性方法 | 含义                                                         |
| -------- | ------------------------------------------------------------ |
| path     | 字符串，表示请求页面的路径，不包含域名                       |
| method   | 字符串，表示页面的请求方法，常用值包括“GET”和“POST"。必须便用大写方式 |
| encoding | 字符串，表示提交的数据的编码方式。一般默认为UTF-8编码方式    |
| GET      | 字典类型，包含 GET请求方法中的所有参数                       |
| POST     | 字典类型，包含POST请求方法中的所有参数                       |
| FILES    | 字典类型，包含上传文件的信息                                 |
| COOKIES  | 字典类型,包含所有的Cookies对象                               |
| session  | 字典类型，表示当前的会话                                     |
| META     | 字典类型，包含所有的HTTP头部信息，如HTTP _USER_AGENT（客户端Agent信息），REMOTE_ADDR（客户端的IP地址）等 |
| user     | 表示当前登录的用户                                           |



### 用法

view.py中

```
def test_get(request):
	print(request.get_host())  # 获取请求的主机名 
	print(request.path)   # 获取请求路径
	print(request.get_full_path()) # 获取请求的完整路径
	print(request.method)    # 表示页面的请求方法
	print(request.GET)  # 包含 GET请求方法中的所有参数
	print(request.build_absolute_uri())  # 构建绝对 URL
	print(request.META['HTTP_USER_AGENT'])  # 客户端信息
	print(request.META['REMOTE_ADDR'])  # 客户端IP地址
	print(request.GET.get('username')) # 'GET'表示获取查询参数，而'username'则指定查询参数的名称
	return HttpResponse('')   # 该行无输出
```

运行，访问`http://localhost:8000/myapp/test_get/`

![image-20230725200611551](https://s2.loli.net/2023/07/25/V7MGDfJveQqYrA6.png)

终端输出

```
localhost:8000
/myapp/test_get/
/myapp/test_get/
GET
<QueryDict: {}>
http://localhost:8000/myapp/test_get/
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183
127.0.0.1
None  
```



## 1.3 `HttpResponse` 对象

每个视图函数都会返回一个`HttpResponse` 对象，对象包含返给客户端的所有数据

常见属性

| 属性         | 含义                                |
| ------------ | ----------------------------------- |
| content      | 返回的内容                          |
| status_code  | 返回的HTTP响应状态码                |
| content-type | 返回的数据MIME类型，默认为text/html |

常见的状态码status_code

| 状态码 | 含义                                  |
| ------ | ------------------------------------- |
| 200    | 状态成功                              |
| 301    | 永久重定向，Location属性的值为当前URL |
| 302    | 临时重定向，Location属性的值为新的URL |
| 404    | URL未发现，不存在                     |
| 500    | 内部服务器错误                        |
| 502    | 网管错误                              |
| 503    | 服务不可用                            |



### 方法write

返回字符串到页面上，可以为HTML代码

在myapp的视图文件里面添加

```
def test_response(request):
	response = HttpResponse()
	response.write('这是通过write方法输出到页面上的文字')
	response.write('<br>')  # 回车
	response.write('这一行也是')
	return response
```

在路由文件中添加路径

```
path('myapp/test_response', views.test_response)
```

运行

![image-20230725204305165](https://s2.loli.net/2023/07/25/sZfJCKxHOXiPGYR.png)



## 1.4 一些视图处理函数

使用HtpRequest和HttpResponse对象，较为繁琐。Django将这些操作进行了封装，提供了几个简单的函数供我们使用。



### 1.4.1 用render()函数实现页面渲染

`render()`函数用于将模板渲染为HTTP响应并返回。它的作用是将请求、上下文和模板结合起来，生成HTML响应。

根据模板文件和 传递给模板文件的字典类型的变量，返回一个HttpResponse对象

函数格式

```
from django.shortcuts import render  # 先导入
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

其中，`request`是必需的，`template_name`也是必需的，而其余参数都是可选的。下面是各个参数的含义：

- `request`: 包含HTTP请求信息的HttpRequest对象。传递给视图函数的所有请求。
- `template_name`: 在templates目录下的模板文件。
- `context`: 字典类型的数据，保存要传递到HTML文件中的变量。默认为None。
- `content_type`: 返回的HTTP响应内容类型。默认为None，即使用默认的content_type，即"text/html"。
- `status`: 返回的HTTP响应状态码。默认为200，也就是None。
- `using`: 指定要使用的模板引擎（如果存在多个模板引擎）用于解析模板文件。默认为None，即使用默认的模板引擎。

### 一个例子

通过字典形式向HTML文件输出数据

myapp1/views.py

```
def test_render(request):
	return render(request, 'myapp1/test_render.html', {'info':'myapp1'}, content_type='text/html')
```

myapp1/urls.py

```
path('myapp1/test_render', views.test_render)
```

在模板中添加myapp1/test_render.html

```
<meta charset="utf-8">
<div>
    myapp1通过render方法输出
    <br>
    {{info}}
</div>
```

运行

![image-20230725221119939](https://s2.loli.net/2023/07/25/8YSgKVMUbx4cP71.png)



### 1.4.2 redirect()实现页面重定向

> 什么是页面重定向？
>
> 页面重定向是指当用户请求一个网页时，服务器将浏览器请求的页面地址重定向到另一个地址，而浏览器会自动跳转到新的页面。常见的页面重定向有 301 重定向和 302 重定向，它们的作用是改变页面的 URL 地址，以及在搜索引擎优化和网站访问性能方面具有重要的作用。例如，将旧的页面地址重定向到新的页面地址可以帮助保持搜索引擎排名和用户访问，也可以帮助在网站更新或迁移时保持页面的访问性能和用户体验。

如果网站的目录结果被调整，网页被移到新地址，若没有重定向，用户通过旧链接，只能得到404。

函数参数有3中情况：

* 通过调用模型的`get_absolute_url()` 函数进行重定向
* 通过路由反向解析进行重定向
* 通过一个绝对的或是相对的URL，让浏览器跳转到指定URL

需要导入

```
from django.shortcuts import redirect
```



### 1.4.3 调用模型函数实现重定向

* 在myapp2中的models.py中添加代码

```
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
    
    # 定义方法，用于返回模型对外的URL
    def get_absolute_url(self):
        return reverse('myapp2_userinfo',kwargs={'id':self.pk}) # 反向解析

    class Meta:
        verbose_name='人员基本信息'
        db_table = 'UserBaseInfo2'
```

> 逐行解释：
>
> 第4~10行：定义一个名为UserBaseInfo的Django模型，它继承自Django内置的models.Model类。
>
> 第5行：定义一个名为id的IntegerField类型的字段，作为该模型的主键
>
> 第6行：定义一个名为username的CharField类型的字段，最大长度为30，作为用户名称字段。
>
> 第7行：定义一个名为password的CharField类型的字段，最大长度为20，作为密码字段。
>
> 第8行：定义一个名为status的CharField类型的字段，最大长度为1，作为状态字段。
>
> 第9行：定义一个名为createdate的DateTimeField类型的字段，它的数据库列名为createDate，用于表示创建日期和时间。
>
> 第11~13行：定义模型的__str__()方法，它返回该模型实例的id。
>
> 第15~19行：定义模型的get_absolute_url()方法，它用于返回该模型对象在网站中的URL地址，其中使用reverse()函数来生成URL。
>
> 第21~23行：定义模型的Meta类，它包含一些元数据，例如verbose_name和db_table属性，分别用于设置模型的人机可读名称和数据库表名。



* 终端运行

```
python .\manage.py makemigrations
python .\manage.py migrate
```

![image-20230802102246455](https://s2.loli.net/2023/08/02/GtRKB5qNaSb23dj.png)

>  这两个命令是 Django 项目中常用的数据库迁移（migration）命令。
>
> `python .\manage.py makemigrations` 的作用是根据您的 Django 项目的 models.py 文件生成数据库迁移文件。这些迁移文件包含您所做的更改（例如增加、修改或删除模型）的详细说明。通过运行这个命令，Django 会自动生成一组迁移文件，并且这些文件会被保存在应用程序的 migrations 目录下。这些迁移文件可以理解为您的数据库模式的版本控制。
>
> `python .\manage.py migrate` 的作用是将生成的迁移文件应用于数据库。这个命令会检查您的 migrations 目录下的所有迁移文件，并将它们应用于数据库。这个命令会自动跟踪每个已经应用的迁移文件，确保所有迁移都被应用。
>
> 通常，您在更改了您的 models.py 文件后，首先应该运行 `python .\manage.py makemigrations` 生成一组迁移文件，然后运行 `python .\manage.py migrate` 将这些迁移文件应用到数据库中。





* 在myapp2的视图文件中添加代码

```
from .models import *
from django.shortcuts import redirect

def test_redirect_model(request,id):
    user=UserBaseInfo.objects.get(id=id)
    return redirect(user)

def userinfo(request,id):
    user=UserBaseInfo.objects.get(id=id)
    return HttpResponse("编号："+str(user.id)+" 姓名："+user.username)
```



* 在myapp2的路由文件中添加代码

```
path('myapp2/test_redirect_model/<int:id>/',views.test_redirect_model,name='app2_test_redirect_model'),
path('myapp2/userinfo/<int:id>/',views.userinfo,name='app2_userinfo'),
```



不断地报错，始终无法解决，先放在这里吧……

![image-20230802123408643](https://s2.loli.net/2023/08/02/38KCYcy7HhMZg4l.png)

崩溃的一上午……



已经解决：原来是表里面没有添加数据

![image-20230803105148183](https://s2.loli.net/2023/08/03/2vATHx7fJKthcrS.png)

添加后，再运行

![image-20230803105206182](https://s2.loli.net/2023/08/03/NsAlGOo8jqYbRHF.png)



### 1.4.4 通过路由反向解析进行重定向

* 打开myapp应用，在views.py中添加函数

```
from django.shortcuts import redirect
def test_redirect_views(request,id):
    return redirect('myapp_userinfo',id)
```

使用redirect函数直接反向解析路由，和reverse()效果一样

* 在urls.py中添加路由

```
path('myapp/test_redirect_views/<int:id>/',views.test_redirect_views,name='app2_test_redirect_views'),
```

* 在views.py中添加跳转重定向函数

```
# 实现跳转重定向
def test_redirect(request):
	return redirect('https://www.cnblogs.com/lmc7/')
```

* 添加对应路由

```
path('myapp/test_redirect/',views.test_redirect,name='app2_test_redirect'),
```

运行

![重定向](https://s2.loli.net/2023/08/02/ANqbvJtf3Qo1nFj.gif)

终端显示

![image-20230802214032329](https://s2.loli.net/2023/08/02/v4XsAInmqRjtKCL.png)





# 2.视图类

另一种处理用户请求的方式，视图类。可以更好地处理不同的HTTP请求。

## 2.1 视图类概述

视图类（CBV)，采用面向对象的思维，把每个方法的处理逻辑变成视图类中的单个方法。

通过在视图类中定义的get()方法和post()方法进行区别。

## 2.2 对比视图函数和视图类

通过视图函数实现对GET,POST请求的接收

```
def index_page(request):
	if request.method == 'GET':
		return HttpResponse('GET请求')
	elif request.method == 'POST':
		return HttpResponse('POST请求')
```

改用视图类的方式，比较简洁：

```
from django.views import View  # 导入
class IndexPageView(View): # 继承于View类
	# 类视图
	def get(self, request):
		return HttpResponse('GET请求')
	def post(self, request):
		return HttpResponse('POST请求')
```

视图类的路由定义方式：

```
from 应用名.views import IndexPageView  # 导入视图类
urlpatterns = [
	path('indexpage/', IndexPageView.as_view())
]
```

视图类在调用时，采用的是函数方式，需要用`as_view()` 将视图类转换为视图函数。



## 2.3 利用视图类进行功能设计

### 2.3.1 通用视图类--TemplateView

用来渲染指定的模板。

新建应用myapp3（记得手动添加），新建文件`view_class.py` ，增加通用视图类

```
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
```

新建路由文件，路由配置（记得在django项目路由文件里面提添加应用分级路由）

```
from django.urls import path
from myapp3.views_class import *
	
# 路径里面添加
urlpatterns = [
    path('myapp3/test_templateview', TestTemplateView.as_view()),
]
```

运行

![image-20230812183211827](https://s2.loli.net/2023/08/12/xVpd7WUm91DOz4u.png)

这里有bug，待解决



### 2.3.2 列表视图类--LiveView

用于将数据表的数据以列表形式显示

在myapp3中的`view_class.py` 添加视图类

```
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
        context["info"]="myapp3: ListView变量可以传递到模板"
        print(context)
        return context
```

* 添加路由

```
path('myapp3/test_listview/',TestListView.as_view()),
```

* 在model.py中添加代码

```
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
        return reverse('app2_userinfo',kwargs={'id':self.pk})

    class Meta:
        verbose_name='人员基本信息'
        db_table = 'UserBaseInfo2'
```

* 新建对应模板文件 `templates/myapp3/test_listview.html`

```
<div>
    接收变量
    <br>
   {{info}}
   <table border=1>
   {% for user in users %}
   <tr>
       <td>{{ user.username }}</td>
       <td>{{ user.status }}</td>
       <td>{{ user.createdate }}</td>
   </tr>
   {% endfor%}
    </table>
    
    <table>
        <tr>
        {% if page_obj.has_previous %}
            <td>
            <a href="?page={{ page_obj.previous_page_number }}">
                上一页
            </a>
            </td>
        {% endif %}
        {% if page_obj.has_next %}
        <td>
            <a href="?page={{ page_obj.next_page_number }}">
                下一页
            </a>
        </td>
        {% endif %}
    </tr>
    </table>
</div>
```

运行

![listview](https://s2.loli.net/2023/08/12/rPoWJlvh7ExwDVS.gif)



### 2.3.4 详细视图类--DetailView

用于将数据表的数据以详细视图的形式显示

在myapp3应用中，views_class.py添加代码

```
class TestDetailView(DetailView):
    model=UserBaseInfo
    template_name="myapp3/test_detailview.html"
    #设置模板变量
    context_object_name="users"
    pk_url_kwarg='userid'
```

配置路由

```
    path('myapp3/test_detailview.html', TestDetailView.as_view()),
```

新建模板 myapp3/test-detail.html

```
<div>
    <br>
   {{info}}
   <table border="1">
    <tr>
        <td>姓名:</td>
        <td>{{ users.username }}</td>
    </tr>
    <tr>
        <td>注册时间:</td>
        <td>{{ users.createdate }}</td>
    </tr>
</table>
</div>
```

运行

