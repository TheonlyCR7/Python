

# 1.1 字符串的基本操作

> 对序列的操作都适用于字符串，但字符串是不可变的，所以元素赋值和切片赋值都是非法的

## 1.1.1 字符串的乘法

```py
str1 = 'hello'
str1 = str1 * 2
print(str1)
> hellohello
```



# 1.2 设置字符串的格式

## 方法一： 使用%来设置字符串

```py
format = 'Hello, %s. %s enough for ya?'
values = ('world', 'Hot') # 元组
print(format % values)
> Hello, world. Hot enough for ya?
```



方法二： 使用模板字符串（需要导入模块）

```py
from string import Template
tmp1 = Template("$test") 
str1 = tmp1.substitute(test = 'yes')
print(str1)
> yes
```

```python
tmpl = Template("Hello, $who! $what enough for ya?")
str1 = tmpl.substitute(who="Mars", what="Dusty")
print(str1)
> Hello, Mars! Dusty enough for ya?
```



## 方法三：使用format

```python
str1 = "{} {} {}".format("1", "2", "3")
print(str1)
> 1 2 3
```

```py
str1 = "I am {}. What is your {}?".format("LMC", "name")
print(str1)
> I am LMC. What is your name?
```

```py
str1 = "{1}, {0}, {2}".format("2", "1", "3")
print(str1)
> 1, 2, 3
```

```py
str1 = "{name} {be} {someone}".format(name = "bob", be = "is", someone = "a dog")
print(str1)
> bob is a dog
```



更完整的设置字符串格式参考：Python基础教程p43



# 1.3 字符串函数

## 1.3.1 endswith 判断最后是否以特定字符串结尾

```py
str1 = 'I am a student'
print(str1.endswith('ent'))
print(str1.endswith('s'))
>
True
False
```



## 1.3.2 chr&ord Unicode的编码与解码

```py
print(chr(65))
> A
print(chr(128584))
> 🙈
```

```py
print(ord(A))
> 65
print(ord(🙈))
> 128584
```

