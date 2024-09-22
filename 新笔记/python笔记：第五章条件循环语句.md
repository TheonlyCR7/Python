# 1.print和import

## 1.1 打印多个参数

同时打印多个表达式，用逗号分隔，逗号会产生空格

```py
print('age:',42)
> age: 42  # 注意 两个表达式之间有空格
```

不加空格的输出方式，加号不会产生空格

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



Python 中的序列解包（也称为序列解构）是一种非常强大且简洁的语法，允许你将一个序列（如列表、元组或字符串）中的元素直接赋值给多个变量。序列解包提高了代码的可读性和简洁性，特别是在处理多变量赋值时。

```python
a, b, c = [1, 2, 3]
print(a)  # 输出: 1
print(b)  # 输出: 2
print(c)  # 输出: 3
```

在这个例子中，列表 `[1, 2, 3]` 被解包，列表的每个元素分别赋值给变量 `a`, `b`, `c`。

**适用于各种序列类型**

序列解包适用于所有序列类型，包括列表、元组、字符串等。

```python
# 解包元组
a, b, c = (1, 2, 3)
print(a, b, c)  # 输出: 1 2 3

# 解包字符串
a, b, c = "abc"
print(a, b, c)  # 输出: a b c

# 解包嵌套序列
(a, b), c = [("x", "y"), "z"]
print(a, b, c)  # 输出: x y z
```



#### 使用星号 `*` 进行扩展解包

星号 `*` 可以用于捕获多余的元素，创建一个列表。

```python
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 输出: 1
print(b)  # 输出: [2, 3, 4]
print(c)  # 输出: 5
```

在这个例子中，变量 `a` 得到第一个元素 `1`，变量 `c` 得到最后一个元素 `5`，变量 `b` 得到中间的所有元素 `[2, 3, 4]`。

**用于交换变量的值**

序列解包常用于交换两个变量的值，而无需使用中间变量。

```python
a = 1
b = 2
a, b = b, a
print(a)  # 输出: 2
print(b)  # 输出: 1
```

**在函数参数中的应用**

序列解包也可以用于函数参数传递，允许将序列的元素作为独立参数传递给函数。

```python
def add(x, y):
    return x + y

numbers = (1, 2)
result = add(*numbers)
print(result)  # 输出: 3
```

在这个例子中，元组 `numbers` 被解包为独立的参数 `1` 和 `2`，并传递给函数 `add`。

**示例：从函数返回多个值**

序列解包常用于从函数返回多个值并将其解包到独立变量中。

```python
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(x)  # 输出: 10
print(y)  # 输出: 20
```

在这个例子中，函数 `get_coordinates` 返回一个元组，元组的元素被解包并赋值给变量 `x` 和 `y`。

**使用 `enumerate` 进行解包**

在迭代过程中，`enumerate` 函数可以生成包含索引和值的元组，这些元组可以被解包。

```python
colors = ['red', 'green', 'blue']

for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")
```

输出：
```
Index: 0, Color: red
Index: 1, Color: green
Index: 2, Color: blue
```

### 在字典中的应用

在遍历字典项时，`items()` 方法返回的键值对元组可以被解包。

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
```

输出：
```
Key: a, Value: 1
Key: b, Value: 2
Key: c, Value: 3
```

### 总结

序列解包是 Python 中一种强大且灵活的特性，可以简化多变量赋值、交换变量值、函数参数传递等操作。它提高了代码的可读性和简洁性，使得处理序列更加直观。无论是在简单的变量赋值，还是在复杂的数据结构处理中，序列解包都是一个非常有用的工具。







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

### 2.2.1  字符串和序列的比较

字符串是根据字符的Unicode码点值排列的，通过ord获取码点值

```PYTHON
print(ord('a'))  // 97
print(ord('z'))  // 122
print(ord('A'))  // 65
print(ord('Z'))  // 90
```

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

`assert` 语句用于进行调试和测试。它会判断一个条件是否为真，如果条件为假，`assert` 语句会触发一个 `AssertionError` 异常。`assert` 通常用于在开发和测试阶段验证程序的状态，确保代码的某些预期条件成立。

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



## 3.2 for循环

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

**for循环的优势之一是，迭代字典时可以使用序列解包**

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

```python
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

让我们逐步分析这段代码。

#### 一个参数

```python
from math import sqrt
exec('sqrt=1')
sqrt(4)
```
**解释：**
1. **导入 `sqrt` 函数**：`from math import sqrt` 导入 `sqrt` 函数，它可以计算平方根。
2. **执行 `exec('sqrt=1')`**：`exec` 函数执行传入的字符串代码。在这里，它将 `sqrt` 变量赋值为 `1`。
3. **调用 `sqrt(4)`**：此时，`sqrt` 已不再是原来的 `sqrt` 函数，而是一个整数 `1`。因此，尝试调用 `sqrt(4)` 就相当于 `1(4)`，这会导致 `TypeError: 'int' object is not callable` 错误，因为整数对象不是可调用的。

#### 两个参数
```python
from math import sqrt
scope = {}
exec('sqrt=1', scope)
print(sqrt(4))
print(scope['sqrt'])
```
**解释：**
1. **导入 `sqrt` 函数**：`from math import sqrt` 导入 `sqrt` 函数。
2. **定义字典 `scope`**：`scope = {}` 创建一个空字典。
3. **执行 `exec('sqrt=1', scope)`**：`exec` 函数在提供的 `scope` 命名空间中执行传入的字符串代码。这意味着 `sqrt=1` 只会在 `scope` 字典中生效，而不会影响全局命名空间中的 `sqrt` 函数。
4. **调用 `sqrt(4)`**：由于全局命名空间中的 `sqrt` 函数未被修改，因此 `sqrt(4)` 调用的是导入的 `math.sqrt` 函数，返回 `2.0`。
5. **打印 `scope['sqrt']`**：这会输出 `1`，因为 `exec('sqrt=1', scope)` 将 `sqrt` 赋值为 `1` 存储在 `scope` 字典中。

**总结：**
- **单参数 `exec`**：直接修改当前作用域中的变量。
- **双参数 `exec`**：将变量绑定到提供的命名空间（字典）中，不会影响当前作用域中的同名变量。

通过这种方式，双参数 `exec` 可以避免对全局命名空间的污染，有助于保持代码的清晰性和安全性。







### 4.3.2 eval

与exec作用类似，但没有返回值

