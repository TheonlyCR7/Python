# 1.网站的入口--路由和视图

URL是网站Web服务的入口。用户在浏览器输入URL发出请求后，django会根据路由系统，运行对应的视图函数，然后返回信息到浏览器中。



## 1.1 认识路由

创建项目时，会自动生成`urls`文件，文件中定义了项目的路由信息，成为项目的路由解析入口。在自建的应用中可以手动配置独立的`urls.py`文件。



### 1.1.1 路由系统的基本配置

urls.py文件

```
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
```

先导入对应的视图函数，然后在`urlpatterns`列表中进行`url`路由配置

path配置语法

```
path(路由, 视图函数, 别名)
```



### 1.1.2 用“路由包含”简化项目复杂度

思路：为每个应用创建一个urls.py文件，将应用的路由配置分别单独放置。

用户发起请求时，会从根路由寻找每个应用的路由信息，生成完整的路由列表。

路由配置规则：

`urlpatterns`列表会从上到下进行匹配

* 匹配成功，会根据视图函数进行跳转
* 匹配失败，则返回404错误

* 若定义了子路由，则在跟路由中使用`include('应用名.urls')` 来加载子路由。如果urls的第一部分被匹配看，则其余部分会在子路由中进行匹配。
* 路由信息一般以`/` 结尾



### 1.1.3 include使用方法

在 Django 项目中，我们可以通过 `URLconf` 文件（即 views.py 文件）来定义路由规则。而在这个 `URLconf` 文件中，我们可以使用 include() 函数来指定自己应该包含的其它 `URLconf` 模块。

通过include可以设置多级路径，语法：

```
path('', include('应用名称.urls'))
```

```
urlpatterns = [
    path('', include('myapp.urls'))
]
```

然后在对应的应用路由文件和视图函数进行配置

myapp的urls.py

```
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
	path('myapp/index/', views.index)
]
```

myapp的views.py

```
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return render(request, 'myapp/index.html')
```

### 1.1.3 实战一下

* 在项目根目录运行

```
python manage.py startapp myapp1
python manage.py startapp myapp2
```

创建两个应用，myapp1 myapp2

* 在项目的路由文件中配置

```
urlpatterns = [
    path('', v.index),  # 这里设置了启动的默认页面
    path('admin/', admin.site.urls),
    path('index/', v1.index, name='index'),
    path('', include('myapp.urls')),
    path('', include('myapp1.urls')),
    path('', include('myapp2.urls'))
]
```

然后在依次对应用的路由和视图函数进行配置（没有则创建）

* 在模板中进行html文件编写

![image-20230722195616877](https://s2.loli.net/2023/07/22/nYigpNmLtDFACsr.png)

* 启动应用

```
python manage.py runserver
```

![image-20230722195632675](https://s2.loli.net/2023/07/22/WHMxUAGQ3oXftEn.png)

![image-20230722195703487](https://s2.loli.net/2023/07/22/KjofqRshwI41ULG.png)

![image-20230722195721157](https://s2.loli.net/2023/07/22/FDNyBcOfGwWX2pQ.png)

![image-20230722195736871](https://s2.loli.net/2023/07/22/7tS91PCVuEF4ReJ.png)



## 1.2 路由参数

我们不可能为所有页面都手动配置路由规则，需要引入URL参数进行动态配置。

### 1.2.1 编写带URL参数的路由

Django动态URL的作用是根据特定的参数动态生成URL。这样，我们可以使用相同的视图函数和模板来处理不同的请求，而不必为每个请求编写单独的视图函数。

这个动态的意思是：根据用户输入的地址信息来显示对应的页面信息。

* 配置

在`myapp`的`urls.py`

```
urlpatterns = [
	path('myapp/index/', views.index),
    path('myapp/show/<int:id>/', views.show),
]
```

在`myapp` 的`views.py`  增加show函数

```
def show(request, id):
	return HttpResponse('myapp中的show方法, 参数为id, 值为' + str(id))
```

* 启动项目

![image-20230722203720851](https://s2.loli.net/2023/07/22/KQbMSskdFXv3E1A.png)

![image-20230722203741144](https://s2.loli.net/2023/07/22/cs8Q1jwrCg2qZOM.png)



### 1.2.2 介绍URL参数

在上面的例子中，路由配置为

```
path('myapp/show/<int:id>/', views.show),
```

`< >` 中的内容就是URL参数，语法：

```
<参数数据类型 : 参数名称>
```

URL参数有4种数据类型

| 参数数据类型 | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| `str`        | 任意非空字符串，不包含`/` ，默认类型                         |
| `int`        | 匹配0和正整数                                                |
| `slug`       | 匹配任何ASCII字符，连接符和下划线                            |
| `uuid`       | 匹配一个UUID格式的字符串，该对象必须包括`-` ，所有字母必须小写。 |



### 1.2.3 [实战] 用`re_path()` 方法正则匹配复杂路由

与path方法作用一样，多了个可以使用正则表达式的功能。

与path一样，使用时，需要导入模块：

```
from django.urls import re_path
```

语法：

```
(?P<name>pattern)   
# name是匹配的字符串名称，pattern是要匹配的模式
# name并不会显示在地址栏中，只有被匹配的字符才会出现在地址栏
# 可以同时有多个表达式，用&连接
```

[点击复习正则表达式]: https://www.cnblogs.com/lmc7/p/17566641.html

**一个例子**

`myapp`应用中，配置urls.py  获取4个数字赋值给year

```
urlpatterns = [
    path('myapp2/index/', views.index),
    re_path(r'myapp2/list/(?P<year>\d{4})/', views.article_list),
]
```

`myapp`应用中，配置views.py

```
def article_list(request, year):
	return HttpResponse("myapp2中的article方法, 参数为year, 指定4位, 值为" + str(year))
```

* 启动

![image-20230722220521548](https://s2.loli.net/2023/07/22/P8dC25NnzAyJGcL.png)

输入超过4个或少于4个 都会访问失败



### 1.2.4 反向解析路由

反向解析路由是指通过给定的URL路径反向得到Django中定义的路由。它的作用是方便在代码中生成URL，而不需要手动拼接URL。

路由正常进行配置

```
path('myapp/url_reverse', views.url_reverse, name = 'myapp_url_reverse')
```

* name后面名称最好为`应用名_视图函数名称`
* name相当于配置项的别名。可以在视图函数或是模板的HTML文件中调用它
* 根据name得到路由配置中的URL地址，这就是 反向解析路由
* 优点：只要name不变，URL地址可以任意改变

**例子**

在`myapp1` 中进行配置

urls.py

```
path('myapp1/url_reverse/', views.url_reverse, name = 'myapp1_url_reverse')
```

views.py

```
from django.urls import reverse # 记得导入
def url_reverse(request):
	# 进行反向解析
	print('反向解析结果：' + reverse('myapp1_url_reverse'))
	return render(request, '2/url_reverse.html')
```

在模板中新建文件 2/url_reverse.html，添加代码

```
<div>
    在HTML中使用url标签进行反向解析
    <br>
    {% url 'myapp1_url_reverse' %}
</div>
```

启动！

![image-20230722232215752](https://s2.loli.net/2023/07/22/Ww3DNmacJS7Hlyb.png)

