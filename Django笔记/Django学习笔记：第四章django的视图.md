# 1. 视图函数

用于处理客户端的请求并生成响应数据。在属兔中使用函数处理请求的方式，被称为视图函数，也叫作FBV(Function Base Views). 

一个简单的视图函数：在views.py里面配置

```
from django.http import HttpResponse  # 导入HttpResponse类

def index(request):  # 接收HttpRequest请求对象
	return HttpResponse('Hello Django!')  # 返回一个HttpResponse对象，包含响应数据
```



## 1.1 视图函数的底层原理

* 主要使用 `HttpRequest` 请求对象和 `HttpResponse` 响应对象。当浏览器向服务端请求一个页面时，Django先创建一个`HttpRequest`对象。
* 当浏览器向服务器发送请求，Django先创建一个HttpRequest对象；
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

```

