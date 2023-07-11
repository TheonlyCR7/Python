---
title: python笔记：第二章基本数据类型
date: 2023-07-05 15:48:22
tags: 
  - python 
  - 学习记录
categories: "python"
---



## 基本数据类型

Python中的数据类型可以分为五大类：字符串、数字、容器、布尔、None

## 1.字符串

可以使用单引号或双引号创建字符串，可以用加号将两个字符串合并

```python3
name = '小明'
age = '9岁'
print('合并字符串:', name + age)
```

格式化字符串：%s

```python3
a = "I'm %s" % ('xiaoming')
print(a)
I'm xiaoming
```

#### 字符串的拼接

```python
x = "first"
y = "blood"
print(x + y)
firstblood
```

#### 格式化表达字符串repr

```python
x = "Hello\nworld"
print(x)
print(repr(x))
print(str(x))
# 输出
Hello
world
'Hello\nworld'   # 格式化输出
Hello
world
```



#### 长字符串

多行表示字符串

```python
x = '''hello! I am a girl.
	what are you looking for?'''
print(x)
hello! I am a girl.
        what are you looking for?
```

> 反斜杠也可以使常规语句跨行

```python
print\
(1 * 7)
7
```

#### 原始字符串

不以特殊方式处理反斜杠，在正则表达式用处很大

> 两种相似类型：不可变的bytes 和 可变的bytearray
>
> 用来与C语言互操作以及将文本写入文件或通过网络套接字发送出去



## 2.整型、浮点型

- 整型：正整数或负整数

```text
number1 = 12        number2 = -3
```

- 浮点型：由整数部分和小数部分组成

```text
score = 96.5
```

- 复数：由实数部分和虚数部分组成



## 3.容器

容器：List(列表)、Tuple(元组)、Sets(集合)、Dictionary(字典)

### List(列表)

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。列表可以修改，可以用于切片、增、删、改、查

```python3
#创建列表
list1 = ['a', 'b', 'c', 'd', 'e']
print(list1)
['a', 'b', 'c', 'd', 'e']
```

```python3
#列表切片
#格式：【start:end:step】
#start:起始索引，从0开始，-1表示结束
#end：结束索引
#step：步长，end-start，步长为正时，从左向右取值。步长为负时，反向取值
#注意切片的结果不包含结束索引，即不包含最后的一位，-1代表列表的最后一个位置索引

a=[1,2,3,4,5,6]
b=a[0:5:3] // 注意是索引，不是顺序
c = a[0:3:1]
print(b)
print(c)
输出结果：
[1, 4]
[1, 2, 3]
```

```python3
#列表删除
del a[-1]  # 删除最后一位 从0开始的序号 -1即为倒数第一位
print(a)
> [1, 2, 3, 4, 5]
del a[-2]
print(a)
> [1, 2, 3, 4, 6]
```

```python
#列表修改
print("未修改之前第一个元素为：",a[0])
a[0] = '66' # 单引号可有可无
print("修改之后第一个元素为：",a[0])
```

```python
#列表查询
a1 = a[0]
print("查询出列表第一个元素为：", a1)
```



### Tuple(元组)

元组和列表类似，但是不同的是元组不能修改，元组使用小括号

```python3
#创建元组
tup = (1, 2, 3, 4, 5)
print(tup)
```

元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用。

```python3
#查询元组,下标索引从0开始
print("查询出列表第一个元素为：", tup[0])
```

元组中的元素值是不允许修改的，但可以对元组进行连接组合

```python3
tup1 = (23, 78);
tup2 = ('ab', 'cd')
tup3 = tup1 + tup2
print (tup3)
(23, 78, 'ab', 'cd')
```



### Sets(集合)

Set是无序的集合，不能有重复的元素，也不能排序

```py
#创建集合
s1 = set(['A','B','C','D'])
print(s1)
# 多次打印的字母顺序都是不同的
{'A', 'C', 'B', 'D'}
{'C', 'B', 'A', 'D'}
{'A', 'D', 'B', 'C'}
```

```python
#增加元素:update
s1.update(['E'])
print(s1)
> {'A', 'D', 'E', 'C', 'B'}
```

```python
#删除元素:discard
s1.discard('E')
print(s1)
```

```python
#修改元素：先删除，后增加
s1.discard('D')
s1.update(['D'])
print(s1)
```

```python
#查询元素
ss = 'B' in s1
print(ss)
> True
bb = 'G' in s1
print(bb)
> false
```



### Dictionary(字典)

字典是另一种可变容器模型，且可存储任意类型对象

字典的格式如下所示：d = {key1 : value1, key2 : value2 }

键必须是唯一的，但值则不必。值可以取任何数据类型，但键的数据类型要保持一致。

```python
#创建字典
d = {'01': 'xiaoming', '02': 'xiaohong', '03': 'xiaowang'}
print(d)
> {'01': 'xiaoming', '02': 'xiaohong', '03': 'xiaowang'}
```

```python
#增加元素
d['04'] = 'xiangfang'
print(d)
> {'01': 'xiaoming', '02': 'xiaohong', '03': 'xiaowang', '04': 'xiangfang'}
d['05'] = 12
print(d)
> {'01': 'xiaoming', '02': 'xiaohong', '03': 'xiaowang', '04': 'xiangfang', '05': 12}
```

```python
#删除元素
del d['04']
print(d)
```

```python
#修改
print("修改之前：",d['01'])
d['01'] = 'xiaolin'
print("修改之后：",d['01'])
```

```python
#查询
d1 = d['01']
print(d1)
> xiaoming
```



## 4.布尔bool

被判定假的有：

```python
False None 0 "" '' () [] {}
```

其他值均视为真True

主要应用在条件判断上面，发生即为True，未发生即为False。Python严格区分大小写，所以一定要注意不要写错。



## 5.None

Python里面特殊的空值，不能理解为0。

