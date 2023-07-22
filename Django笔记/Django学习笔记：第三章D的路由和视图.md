# 1.网站的入口--路由和视图

URL是网站Web服务的入口。用户在浏览器输入URL发出请求后，django会根据路由系统，运行对应的视图函数，然后返回信息到浏览器中。



## 1.1 认识路由

创建项目时，会自动生成urls.文件，文件中定义了项目的路由信息，成为项目的路由解析入口。在自建的应用中可以手动配置独立的urls.py文件。



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



### 1.1.3 实战一下

在项目根目录运行

```
python manage.py startapp myapp2
```

![image-20230722113051495](https://s2.loli.net/2023/07/22/YgitOS6zobIavJx.png)

打开项目路由文件，配置

```
from django.contrib import admin
from django.urls import path
from myapp2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', include('myapp.urls')),
    path('', include('myapp2.urls'))
]
```

进入myapp2文件夹中，创建urls.py

![image-20230722113307481](https://s2.loli.net/2023/07/22/6xtN7BJjOmgsTH8.png)

添加配置

```
from django.contrib import admin
from django.urls import path
from myapp2 import views

urlpatterns = [
    path('myapp2/index/', views.index),
]
```

打开应用的视图文件view，添加代码

```
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("myapp2中的index")
```

