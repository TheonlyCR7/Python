## 1.1 概述

> 说白了就是键值对的映射关系
>
> 不会丢失数据本身关联的结构，但不关注数据的顺序
>
> 是一种可变类型

```py
格式：dic = {键:值, 键:值}
```

* 键的类型：字典的键可以是任何不可变的类型，如浮点数，字符串，元组

## 1.2 函数dict

可以从其他映射或键值对创建字典

```py
items = [('name', 'Gumby'), ('age', 42)]
d =dict(items)
print(d)
> {'name': 'Gumby', 'age': 42}
```

```py
d = dict(name='Gumby', age=42)
print(d)
> {'name': 'Gumby', 'age': 42}
```



## 1.3 字典的基本操作

```py
num = len(d) # 返回字典的键值对数量
str1 = d[键] # 参数为键 返回值为对应的值
d[键] = '值' # 将tom赋值给name1键
test = 键 in 字典名字 # 检查name3键是否在字典中
```

```py
d = {
    'name_a' :'Gumby', 'age1':42, 
    'name_b' :'bob', 'age2':12, 
    'name_c':'lily', 'age3':14}
num = len(d) # 返回字典的键值对数量
print('num=' + str(num))
> num=6
str1 = d['name_a'] # 参数为键 返回值为对应的值
print('name_a=' + str1)
> name_a=Gumby
d['name_a'] = 'tom' # 将tom赋值给name1键
print('name_a=' + d['name_a'])
> name_a=tom
test = 'name_c' in d # 检查name3键是否在字典中
print(test)
> True
```



## 1.4 与format相结合

>  将字符串格式设置功能用于字典

使用format_map将两者结合起来

```py
phonebook = {'bob' : 1211, 'tom': 2322}
str1 = "I am bob. My phone is {bob}".format_map(phonebook)
print(str1)
> I am bob. My phone is 1211
```



## 1.5 字典常用方法

### 1.5.1 clear删除所有字典项

就地执行，无返回值

```py
d = {
    'name_a':'Gumby', 'age1':42, 
    'name_b':'bob', 'age2':12, 
    'name_c':'lily', 'age3':14}
d.clear()
print(d)
> {}
```

> python中的变量赋值，是将变量名指向该地址，对该变量名的字典操作，实际上是对该地址存储的字典进行操作，如：
>
> ```py
> d = {
>     'name_a' :'Gumby', 'age1':42, 
>     'name_b' :'bob', 'age2':12, 
>     'name_c':'lily', 'age3':14}
> x = d
> x.clear()
> print(x)
> print(d)
> > {}
> > {}   # 发现两个字典均被清空
> ```
>
> 若将x再次赋其他值，对原来的字典没有影响
>
> ```py
> d = {
>     'name_a' :'Gumby', 'age1':42, 
>     'name_b' :'bob', 'age2':12, 
>     'name_c':'lily', 'age3':14}
> x = {}
> x.clear()
> print(d)
> print(x)
> >
> {'name_a': 'Gumby', 'age1': 42, 'name_b': 'bob', 'age2': 12, 'name_c': 'lily', 'age3': 14}
> {}
> ```



### 1.5.2 copy浅复制与深复制

#### 浅复制

返回一个新字典，与原来的字典完全相同（浅复制）

```py
d = {
    'name_a' :'Gumby', 'age1':42, 
    'name_b' :'bob', 'age2':12}
x = d.copy()
print(d)
print(x)
> 
{'name_a': 'Gumby', 'age1': 42, 'name_b': 'bob', 'age2': 12}
{'name_a': 'Gumby', 'age1': 42, 'name_b': 'bob', 'age2': 12}
```

浅复制要分两种情况进行讨论：

1）当浅复制的值是不可变对象（字符串、元组、数值类型）时和“赋值”的情况一样，对象的id值（id()函数用于获取对象的内存地址）与浅复制原来的值相同。

2）当浅复制的值是可变对象（列表、字典、集合）时会产生一个“不是那么独立的对象”存在。有两种情况：

* 第一种情况：复制的对象中无复杂子对象，原来值的改变并不会影响浅复制的值，同时浅复制的值改变也并不会影响原来的值。原来值的id值与浅复制原来的值不同。

* 第二种情况：复制的对象中有复杂子对象（例如列表中的一个子元素是一个列表），如果不改变其中复杂子对象，浅复制的值改变并不会影响原来的值。 但是改变原来的值中的复杂子对象的值会影响浅复制的值。

参考：[Python中的赋值(复制)、浅拷贝与深拷贝 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/54011712)

#### 深复制

模块copy中的`deepcopy` 可以同时复制值以及包含的所有值

```py
from copy import deepcopy
d = {
    'name_a' :'Gumby', 'age1':42, 
    'name_b' :'bob', 'age2':12}
x = deepcopy(d) # 深
y = d.copy() # 浅
x.clear()
print(d)
print(y)
```



### 1.5.3 fromkeys 按条件创建字典

创建一个新字典，其中包含指定的键，且每个键对应的值都是None

```py
d = dict.fromkeys(['name','age'])
print(d)
> {'name': None, 'age': None}
```

若不想使用默认值None 可以提供特定的值

```py
d = dict.fromkeys(['name','age'], 'default')
print(d)
> {'name': 'default', 'age': 'default'}
```



### 1.5.4 get 通过键获取值

原来的直接通过键获取对应的值时，可能因为字典中没有该键而报错。

```py
d = dict.fromkeys(['name','age'], 'default')
print(d['weight'])
> 
    print(d['weight'])
          ~^^^^^^^^^^
KeyError: 'weight'
```

而get方法下，寻找不存在的键值时，会返回None（可指定），不会报错

```python
d = dict.fromkeys(['name','age'], 'default')
print(d.get('weight'))
> None
```

指定失败返回值为 N/A (可用于返回错误信息)

```PY
d = dict.fromkeys(['name','age'], 'default')
print(d.get('name', 'N/A'))
> N/A
```

查找成功，正常返回对应值

```PY
d = dict.fromkeys(['name','age'], 'default')
print(d.get('name', 'N/A'))
> default
```



### 1.5.5 items 将字典变成列表输出

返回一个包含所有字典项的列表，其中每个元素都为(key, value)的形式，顺序不固定

```py
d = {
    'name_a' :'Gumby', 'age1':42, 
    'name_b' :'bob', 'age2':12}
li = d.items()
print(li)
> dict_items([('name_a', 'Gumby'), ('age1', 42), ('name_b', 'bob'), ('age2', 12)])
```

返回值属于字典视图的特殊类型，特点是不复制，始终是原字典的反映，随原字典改变而改变

```py
d['name_a'] = 'tom' # 修改原字典
print(li)
> 
dict_items([('name_a', 'tom'), ('age1', 42), ('name_b', 'bob'), ('age2', 12)])
```



### 1.5.6 keys 返回字典的键

返回值为字典视图

```py
d = {
    'name_a' :'Gumby', 'age1':42, 
    'name_b' :'bob', 'age2':12}
li = d.keys()
print(li)
> dict_keys(['name_a', 'age1', 'name_b', 'age2'])
```



### 1.5.7 pop获取键对应的值，并删除键值

```py
d = {'name_a' :'Gumby', 'age1':42}
li = d.pop('name_a')
print(li)
print(d)
>
Gumby
{'age1': 42}
```



### 1.5.8 popitem “弹出”一组键值对

返回一组键值对，并从字典中删去该键值对，与列表中的pop方法类似，只是字典没有最后一位的概念

> 书上说这里会随机弹出，但实际运行情况是弹出最后一对。查了一下文档，发现python3.6以后不再是随机弹出，即弹出最后一对

```py
d = {'name_a' :'Gumby', 'age1':42}
print(d.popitem())
print(d.popitem())
print(d)
> 
('age1', 42)
('name_a', 'Gumby')
{}
```

```py
d = {'name_a' :'Gumby', 'age1':42}
d_len = len(d.items())
print(d_len)
i = 0
while(i < d_len):
    print(d.popitem())
    i = i + 1
> 
2
('age1', 42)
('name_a', 'Gumby')
```



### 1.5.9 setdefault 获取指定键值 无则添加

有点像get 但对于找不到指定的键时，会添加指定的键值

```py
d = {}
print(d.setdefault('name', 'None'))
print(d)
> 
None
{'name': 'None'}
```



### 1.5.10 update 使用A字典的项更新B字典

```python
d1 = {'name': 'bob', 'age': 12}
d2 = {'name': 'tom'}
d1.update(d2)
print(d1)
> {'name': 'tom', 'age': 12}
```



### 1.5.11 values 返回字典的值

不同于键的唯一性，values的返回值可能有相同值

```py
d1 = {'name': 'bob', 'age': 60, 'weight': 60}
print(d1.values())
dict_values(['bob', 60, 60])
```

返回类型同样为字典视图