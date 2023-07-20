# 1.模块

```
import 模块名
```



## 1.1 模块就是程序

任何python程序都可以作为模块导入，并标明程序（模块）的位置

```
import sys
sys.path.append('路径')
```

```
import hello  // 在同一文件夹下
```

会在该文件夹里面自动生成一个`__pycache__` 文件夹，包含处理后的文件。（可删除，无影响）

![image-20230717212214673](https://s2.loli.net/2023/07/18/4oiuVKhwJa56fDA.png)

在hello.py里面编写函数

![image-20230717212505923](https://s2.loli.net/2023/07/18/eWVpsI3zORfd1Lg.png)

在t13.py里面调用模块函数

```
import hello
hello.hello1()
```

运行结果

```
hello
hello!
```



## 1.2 模块属性

### 1.2.1 __name__

检查模块是作为程序运行还是被导入到另一个程序

如：在t13文件中，查看name属性

```
print(__name__)
> __main__
```

在t13文件中，查看hello文件的name属性

```
print(hello.__name__)
> __hello__
```



### 1.2.2 dir

查明模块包含哪些东西，列出对象的所有属性（函数，类，变量）

```
print(dir(模块名))
```

```
import box.shapes as sh
print(dir(sh))
```

```
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
```



### 1.2.3 变量`__all__`

用于指定一个模块的所有公共接口（方法），只有被`__all__`指定的接口，才可以被正确导入。

module.py

```
__all__ = ['foo', 'bar']

def foo():
    print("This is foo!")

def bar():
    print("This is bar!")

def baz():
    print("This is baz!")
```

main.py

```
from module import *

foo()  
bar()  

baz()  
```

运行main.py结果

```
This is a foo!
This is bar!
NameError: name 'bar' is not defined
```



1.2.4 文档`__doc__`

查看模块信息和函数信息

```
print(range.__doc__)
```

```
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
```



**自定义文档字符串**

通过三引号的方式添加

```
def plus(a, b):
	'''This is a plus'''
	print(a + b)

print(plus.__doc__)
> This is a plus
```



### 1.2.4 获取模块路径`__file__`

可以获取当前模块所在的目录或文件的绝对路径。

如main.py

```
print(__file__)
> d:\M\github\Python\Demo\main.py
```

还可以使用`os.path`模块的方法对路径进行处理，例如获取当前模块**所在目录**的绝对路径：

```
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
print(module_dir)
> d:\M\github\Python\Demo
```



# 2.包

包可以包含其他模块，模块存储在扩展名为.py的文件中，包则是一个目录。

包必须包含有`__init__.py`文件

 ![image-20230718171439433](https://s2.loli.net/2023/07/18/2HN6rP819gpWKqR.png)

在与文件夹box的同级文件下可以导入

```
import box
import box.shapes
```



# 3.一些重要的模块

## 3.1 sys



## 3.2 os

## 3.3 fileinput

## 3.4 集合，堆和双端队列

## 3.5 time

## 3.6 random

## 3.7 shelve和json

## 3.8 re

re，即正则表达式模块
