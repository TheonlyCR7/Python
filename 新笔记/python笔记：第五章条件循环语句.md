# 1.print和import

## 1.1 打印多个参数

同时打印多个表达式，用逗号分隔

```py
print('age:',42)
> age: 13  # 注意 两个表达式之间有空格
```

不加空格的输出方式

```py
print('block' + 'chain')
> blockchain
```

自定义分隔符

```py
print('L', 'M', 'C', sep='-')
> L-M-C
```

自定义结束字符串（默认为换行符）

```py
print('I am a student')
print('I am a student', end = '.')
print('Yes')
>
I am a student
I am a student.Yes
```



## 1.2 导入时重命名

导入模块方法通常有

```py
import module
from module import function
from module import function1, function2, function3
from module import *  # 当且仅当需要导入模块的一切时
```

若导入的两个模块具有同名函数时，进行区分调用

方法一：

```py
module1.function()
module2.function()
```

方法二：导入时对模块或方法重命名

```py
import math as bobo
bobo.sqrt(4)
> 2
```

```py
from math import sqrt as popo
popo(4)
> 2
```

对于前面的不同模块的相同函数，可以这样导入：

```py
from module1 import open as open1
from module2 import open as open2
```



## 1.3 赋值的多种方法

### 1.3.1 序列解包

* 同时给多个变量赋值

```py
x, y, z = 1, 2, 3
print(x, y, z)
> 1, 2, 3
```

* 同时赋值时，对象可以是元组。

```py
x, y, z = (1, 2, 3)
print(x, y, z)
> 1, 2, 3
# 但要保证等号左右两侧数量一致
x, y, z = (1, 2, 3, 4)
> ValueError: too many values to unpack (expected 3)
```

* 可以采用星号*来收集多余的值，这样便无需两者一致
```py
x, y, *r = (1, 2, 3, 4)
print(x, y)
print(r)
> 
1 2
[3, 4]

x, *r, y = (1, 2, 3, 4)
print(x, y)
print(r)
> 
1, 4
2, 3
```

> 赋值语句右边可以是任何类型的序列，但*变量总是变成一个列表

* 赋值特性在元组解包时效率很高

```py
stbook = {'name': 'bob', 'age': 12}
name, age = stbook.popitem()
print(name, age)
```


* 交换变量值

```py
x, y, z = 1, 2, 3
x, y = y, x
print(x, y)
> 2, 1
```

```py
x, y, z = 1, 2, 3
z, x, y = x, y, z
print(x, y, z)
> 2 3 1
```



### 1.3.2 链式赋值

```py
x = y = 1
```



### 1.3.3 增强赋值

代码更加紧凑，增加可读性

```
x += 1
x *= 1
'hello' * 2
```



# 2.条件语句

代码块：python中的代码块是通过缩进来实现的

## 2.1条件语句

语句结构（注意缩进）

```
if 判断体:
	代码块
else:
	代码块
```

```python
if 判断体:
	代码块
elif 判断体:
	代码块
else:    # 可有可无
	代码块
```

可以进行条件嵌套

## 2.2 比较运算符

常用的有：

```python
== > < >= <= != 比较常见
x is y # x和y是同一对象
x is not y # x和y是不同的对象
x in y # y是一个容器，x是其中的一个元素
x not in y # y是一个容器，x不是其中的一个元素
```

> 要注意区分 == 和is 前者检查两个对象是否相等（值相同），后者是检查是否为同一对象

### 2.2.1字符串和序列的比较

字符串是根据字符的码点排列的，通过ord获取码点值

```python
str1 = bool('a' > 'B')
print(str1)
> True
```

* lower()函数，忽略大小写，进行比较

```python
bo = 'b'.lower() = 'B'.lower()
print(bo)
> True
```

* 其他类型的序列也可以比较

```py
a = [1, 2]
b = [1, 3]
bo = a > b
print(bo)
> False
```



## 2.3 布尔运算符

and or

```python
a = int(input("a = "))
if a < 10 and a > 0:  # 或是用链式 0 < a < 10
	print("Great!")
else:
	print("wrong!")
>
a = 2
Great!
```

```python
a = int(input("a = "))
if a > 10 or a < 0:
	print("Great!")
else:
	print("wrong!")
> 
a = -1
Great!
```

> 对于 表达式 and 表达式，表达式 or 表达式 的判断采用的是“懒惰"逻辑



## 2.4 断言 assert

类似于给程序设置断点，充当检查点

```python
age = 10
asert 0 < age < 100
print('age =', age)
age *= 10
assert 0 < age < 100 # 这里会断
print('age =', age)
> 
age = 10
Traceback (most recent call last):
  File "d:\M\github\Python\Demo\t8.py", line 41, in <module>
    assert 0 < age < 100
           ^^^^^^^^^^^^^
AssertionError
```

还可以对断点做出说明

```python
age = 24
assert age < 18, "He is not a boy!"
> 
AssertionError: He is not a boy!
```



# 3.循环语句

## 3.1while 循环

```python
x = 2
while x > 1: # 先判断 再执行代码块
	print(x)  
	x += 1
```

```python
name = ''
while not name:
    name = input('Please enter your name: ')
print('Hello, {}!'.format(name))
>
Please enter your name: 
Please enter your name: lmc
Hello, lmc!
```



## 3.2for循环

使用起来和java中的非常像，多用于序列的迭代

```python
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
	print(word)
```



### 3.2.1 范围函数range

```
range(起始位置, 结束位置)  这个范围包括起始位置，不包括结束位置
```

```python
for num in range(0, 3):
    print(num, end=' ')
> 0 1 2
```

> 优先使用for循环，while次之



### 3.2.2 迭代字典

```python
d = {'x': 1, 'y': 2}
for key in d: # key获取的是键
    print(key, 'to', d[key])
>
x to 1
y to 2
```

for循环的优势之一是，迭代字典时可以使用序列解包

```python
d = {'x': 1, 'y': 2}
for key, value in d.items():
	print(key, 'to', value)
> 
x to 1
y to 2
```



## 3.3 break和continue

* break: 跳出当前循环
* continue:结束当前迭代，进入下一次循环

### 3.3.1 使用技巧：while true

```python
while True:
	word = input("enter a word: ")
	if not word: break  # 及时结束循环
	print(word)
```



## 3.4 与else语句搭配

for，while循环均可搭配

```python
for n in range(10):
    if n > 10: break
else: # 仅当break没运行的时候 才运行
    print("else exe")
> else exe
```

```python
# 想找到90
for n in range(100):
    if n == 10*9: 
    	print("Yes")
    	break
else:
    print("None")
> Yes
```



# 4.三个趣味函数

## 4.1 pass 啥都不做

用于占位，让程序可以试运行

```python
if name == 'bob':
	pass
else:
	print("Wrong!")
```

也可用于构造函数

## 4.2 del 删除

在python中，无法删除值，也无需删除值（python解释器会为你做好垃圾回收），删除的只是引用 ，只是变量名罢了

```python
x = y = 'python'
del x
print(y)
print(x)
>
python
NameError: name 'x' is not defined
```



## 4.3 exec和eval

### 4.3.1 exec

可将字符串作为代码执行

```py
exec("print('look')")
> look
```

只给一个参数不够安全，会污染命名空间（待填坑），应该设置一个域名空间，用于放置变量

```py
# 一个参数
from math import sqrt
exec('sqrt=1')
sqrt(4)
> TypeError: 'int' object is not callable

# 两个参数
from math import sqrt
scope = {}
exec('sqrt=1', scope)
print(sqrt(4))
print(scope['sqrt'])
>
2.0
1
```



### 4.3.2 eval

与exec作用类似，但没有返回值
