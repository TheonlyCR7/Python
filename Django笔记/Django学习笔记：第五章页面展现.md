# Django学习笔记：第五章页面展现--基于Django模板

Django提供了模板技术用于编写HTML代码，之后可以通过视图技术渲染模板将最终生成的HTML代码返给客户端浏览器进行显示。

Django模板技术分为两部分：

* 静态，如HTML, CSS, JS
* 动态，如Django的模板语言DTL

## 1.Django模板语言--DTL

Django模板是一种带有DTL语言的HTML文件，这个文件可以被Django编译，可以传递参数，实现数据动态化。

该语言包括模板变量，模板标签和模板过滤器。



## 1.1 模板变量

模板变量，可以是字符串，列表，字典，类对象

模板变量类似于占位符的作用：当执行时，会动态替换



### 1.1.1 变量的表示

模板变量使用`{{ 变量名 }}` 来表示，注意：在变量名前后都有空格与大括号分开

名字可以由字母数字下划线组成

```
{{ age }}  {{ name }}
```



### 1.1.2 实例

在myapp3中的视图文件，增加函数

```
def var(request):
   #v=PersonInfo.objects.all()
   #print(v)
   #列表对象
   lists=['Java','Python','C','C#','JavaScript']
   #字典对象
   dicts={'姓名':'张三','年龄':25,'性别':'男'}

   return render(request,'3/var.html',{'lists':lists,'dicts':dicts})
```

