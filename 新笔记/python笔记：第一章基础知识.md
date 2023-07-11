---
title: python笔记：第一章基础知识
date: 2023-07-04 16:12:15
tags: 
  - python 
  - 学习记录
categories: "python"
---





## 利用python交互式应用

搜索找到py即可

![image-20230704161438688](https://s2.loli.net/2023/07/05/W8byY7IhsEiVDKz.png)

或是在终端运行python

![image-20230704161503827](https://s2.loli.net/2023/07/05/YHM6zVxjS2Z8kE4.png)

<!--more-->

## 1.概述

* python是个面向对象的脚本语言
* 与工业语言不同，每行无需分号，无需大括号
* 使用的是`Unicode` 编码来表示文本
* 严格区分大小写
* 用缩进来区分代码块



运算符在python中同样成立

![image-20230704161827316](https://s2.loli.net/2023/07/05/8tHOgpvyT3k2r1e.png)

### 1.1变量

同样地，变量的命名只能由字母，数字和下划线构成。不能以数字开头。

* 在使用python变量前，必须要赋值，因为python中的变量没有默认值



### 1.2 语句

语句和表达式



### 1.3 获取用户输入

```python
>>> input("your name is ")
your name is bob
'bob'
```

```python
x = input()
y = input()
print(x * y)   
// 会报错
Traceback (most recent call last):
  File "d:\M\github\Python\Demo\t1.py", line 3, in <module>
    print(x * y)
          ~~^~~
TypeError: can't multiply sequence by non-int of type 'str'
```

说明接受用户输入的是字符串类型str

```
x = input()
y = input()
print(int(x) * int(y))  // 转为int型
1
2
2
```



### 1.4 函数

* 分为内置函数和自定义函数

* 进行幂运算的函数

  ```
  print(2 ** 3)
  8
  // 或是使用函数pow
  pow(2, 3)
  8
  ```

* abs计算绝对值

  ```
  print(abs(-10))
  10
  ```

* round 化整函数 

  ```
  // 将浮点数化整为最接近的整数
  print(round(1.2))
  print(round(1.5))
  print(round(1.9))
  1
  2
  2
  ```



### 1.5 模块

模块，也称扩展，可以扩展python功能 关键字 `import`

使用方法：`模块名.方法名` 

```python
import math
math.floor(32.9) # 向下取整
32
math.ceil(32.9) # 向上取整
33
```

精确地导入某个函数

```python
from math import sqrt
print(sqrt(9))  # 无需模块名 计算平方根
3.0
```

