# 1.模块re

- 以一定规则，快速检索文本，或是实现一些替换操作
- 默认下，区分大小写

# 2.常见的匹配字符表

|   字符   |                             描述                             |
| :------: | :----------------------------------------------------------: |
|    \d    |            代表任意数字，就是阿拉伯数字 0-9 这些             |
|   `\D`   |                代表非数字的字符。与\d完全相反                |
|   `\w`   |       代表字母，数字，下划线。也就是 a-z、A-Z、0-9、_        |
|   `\W`   |   跟 \w 相反 ，代表不是字母，不是数字，不是下划线的字符。    |
|    \n    |                        代表一个换行。                        |
|   `\r`   |                        代表一个回车。                        |
|   `\f`   |                          代表换页。                          |
|   `\t`   |                       代表一个 Tab 。                        |
|   `\s`   |    代表所有的空白字符，也就是上面这四个：\n、\r、\t、\f。    |
|   `\S`   |             跟 \s 相反，代表所有不是空白的字符。             |
|   `\A`   |                      代表字符串的开始。                      |
|   `\Z`   |                      代表字符串的结束。                      |
|    ^     |                    匹配字符串开始的位置。                    |
|    $     |                    匹配字符创结束的位置。                    |
|    .     |                代表所有的单个字符，除了 \n \r                |
| `[...]`  |     代表在 [] 范围内的字符，比如 [a-z] 就代表 a到z的字母     |
| `[^...]` |          跟 [...] 唱反调，代表不在 [] 范围内的字符           |
|   {n}    | 匹配在 {n} 前面的东西，比如: o{2} 不能匹配 Bob 中的 o ，但是能匹配 food 中的两个o。 |
| `{n,m}`  | 匹配在 {n,m} 前面的东西，比如：o{1,3} 将匹配`fooooood`中的前三个o。 |
| `{n，}`  | 匹配在 {n,} 前面的东西，比如：o{2,} 不能匹配“Bob”中的“o”，但能匹配`fooooood`中的所有o。 |
|   `*`    | 和 {0,} 一个样，匹配 * 前面的 0 次或多次。 比如 zo* 能匹配“z”、“zo”以及“zoo”。 |
|   `+`    | 和{1，} 一个样，匹配 + 前面 1 次或多次。 比如 zo+”能匹配“zo”以及“zoo”，但不能匹配“z”。 |
|   `？`   |          和{0,1} 一个样，匹配 ？前面 0 次或 1 次。           |
|   a\|b   |                       匹配 a 或者 b。                        |
|  `（）`  |                     匹配括号里面的内容。                     |



```python
a = 'C|C++|C#|Python|Java'
# 判断字符串 a 中是否含有 Python
print(a.index('Python')>-1)   #  True
print('Python' in a)   #  True

import re

re.findall('Python', a)  #  在字符串 a 中，找到所有的'Python'字符串
print(re.findall("Python", a))  #  ['Python']
```

## 2.1`/d /D`

```python
import re
a = 'C0C++1C#2Python3Java'
# 检索所有数字
r = re.findall('\d', a)  #  \d 匹配所有数字  元字符的一种
print(r)  
> ['0', '1', '2', '3']

r = re.findall('\D', a)  #  \d 匹配所有非数字  元字符的一种
print(r)  
> ['C', 'C', '+', '+', 'C', '#', 'P', 'y', 't', 'h', 'o', 'n', 'J', 'a', 'v', 'a']
```

## 2.2`[]`  表示或


```python
[]  表示或
import re
s = 'abc, acc, adc, aec, afc, ahc'
r = re.findall('a[cf]c', s) # 匹配中间是 c 或 f 的字符串
print(r)  
> ['acc', 'afc']

[^]   表示否定
r = re.findall('a[^cf]c', s) # 匹配中间不是 c 和 f 的字符串
print(r)  
> ['abc', 'adc', 'aec', 'ahc']

#  [c-f]   匹配c 到 f 的所有字符
r = re.findall('a[c-f]c', s) # 匹配 c 到 f 的字符
print(r)  
> ['acc', 'adc', 'aec', 'afc']
```

## 2.3`\w \W`


```python
# 概括字符集
# \w   \W
import re
a = 'C0C++\n1C# 2Python3*Java_'

r = re.findall('\w', a) # 匹配数字和字母  相当于  [A-Za-z0-9_]
print(r)  
> ['C', '0', 'C', '1', 'C', '2', 'P', 'y', 't', 'h', 'o', 'n', '3', 'J', 'a', 'v', 'a', '_']

r = re.findall('\W', a)  # 非单词非数字字符  
print(r)  
> ['+', '+', '\n', '#', ' ', '*']

# \s  空白字符
r = re.findall('\s', a) 
print(r)  
> ['\n', ' ']
```

## 2.4`{}`  表示匹配次数


```python
# 数量词  
#  {4}   4 表示每次匹配次数 
import re
a = 'python 11 java 22 php'
r = re.findall('[a-z]{3}', a) # 匹配三个连续字母
print(r)  
> ['pyt', 'hon', 'jav', 'php']

# {3, 6}  表示匹配次数在 3到6 之间
r = re.findall('[a-z]{3,6}', a)  # 匹配长度在3-6之间的单词
print(r)  
> ['python', 'java', 'php']
```

## 2.5贪婪 非贪婪`？`


```python
# 贪婪 非贪婪 
# python 默认为贪婪模式  尽可能 多匹配 和 多次匹配
# 非贪婪模式  表达式后面加 ？ 匹配最少的次数
r = re.findall('[a-z]{3,6}?', a)
print(r)  
> ['pyt', 'hon', 'jav', 'php']
```

## 2.6`*`  `+`

```python
# * 匹配前面的一个字符 0 次或者无限多次
a = 'pytho0python1pythonn2'
r = re.findall('python*', a) # 与 * 紧挨的字符n 匹配0次或是无限多次
print(r) 
> ['pytho', 'python', 'pythonn']

r = re.findall('pytho*', a) # 与 * 紧挨的字符n 匹配0次或是无限多次
print(r) 
> ['pytho', 'pytho', 'pytho']

r = re.findall('pythonn*', a) # 与 * 紧挨的字符n 匹配0次或是无限多次
print(r) 
> ['python', 'pythonn']

# + 匹配一次或无限多次
import re
a = 'pytho0python1pythonn2'
r = re.findall('python+', a) # 与 + 紧挨的字符n 匹配1次或是无限多次
print(r) 
> ['python', 'pythonn']

# 不加 ?  
r = re.findall('python{1,2}', a) # 匹配n 出现一次到两次
print(r) 
> ['python', 'pythonn']

# 加了 ?  设置为非贪婪模式
r = re.findall('python{1,2}?', a) # 匹配n 出现一次
print(r) 
> ['python', 'python']
```

## 2.7`^ $`  边界符

```python
# 边界匹配
import re
qq = '1000001'

r = re.findall('\d{4,8}', qq) # 匹配4 到8 位的QQ号
print(r)  
> ['1000001']

qq = '10000000001'
r = re.findall('\d{4,8}', qq) # 匹配4 到8 位的QQ号
print(r)  # ['1000001']     没有达到目的

# ^ $ 边界符  
# ^ 规定以什么开始
# $ 规定以什么结束
r = re.findall('^\d{4,8}$', qq) # 匹配4 到8 位的QQ号
print(r)  # []   没有匹配到

r = re.findall('^0000', qq) # 匹配从 0 开始的字符串
print(r)  # []   没有匹配到
```

## 2.8`()`  分组

```python
# ()  一个括号对应一组
import re
a = 'pythonpythonpythonJs'

r = re.findall('(python){3}(JS)', a)
print(r)  
> []

# re.I 不区分大小写  第三个参数
r = re.findall('(python)(JS)', a, re.I)
print(r)  
> [('python', 'Js')]

# 接受多个第三个参数时，用|隔开
r = re.findall('(python)(JS)', a, re.I | re.S)
print(r)  
> [('python', 'Js')]
```

## 2.9`.` 匹配除换行符\n 以外的其他所有字符

```python
# . 匹配出换行符\n 以外的其他所有字符
a = 'python\nCC'
r = re.findall('python.', a, re.I)  # 无法匹配\n
print(r)  
> []   

r = re.findall('python.', a, re.S)   #  让 . 可以匹配换行符 
print(r)  
> ['python\n']   
```

## 2.10`re.sub` 替换操作

```python
# re.sub 替换操作
import re
language = 'PythonC#JavaC#PHPC#'
r = re.sub('C#', 'GO', language)
print(r)   
> PythonGOJavaGOPHPGO

r = re.sub('C#', 'GO', language, 1)
print(r)   
> PythonGOJavaC#PHPC#   只替换了一个

r = re.sub('C#', 'GO', language, 0)
print(r)   
> PythonGOJavaGOPHPGO

# re.sub 的第二个参数可以是函数
def convert(value):
    pass
r = re.sub('C#', convert, language)
print(r)  
> PythonJavaPHP


def conver(value):
    matched = value.group()
    return '!!' + matched + '!!'

r = re.sub('C#', convert, language)
print(r)   
> Python!!C#!!PHP!!C#!!
```

## 2.11将函数作为参数


```python
# 将函数作为参数
import re
s = 'ABC37978D432'

def convert(value):
    # 拿到具体数字
	matched = value.group()
	if matched >= 6:
        return 9
    else:
        return 0
    
r = re.sub('\d', convert, s)
print(r)  
> ABC09999D000
```

## 2.12`re.match  re.search` 

```python
# re.match
# re.search    
# 都返回类对象
import re
s = 'ABC37978D432'

r = re.match('\d', s)  #  从字符串的开始位置开始匹配，若不符，则返回None
print(r)  
> None

r = re.search('\d', s) #  在字符串中寻找可以匹配的
print(r)  
> <re.Match object; span=(3, 4), match='3'>

print(r.group())  # 3
print(r.span())   # (3, 4)   返回匹配的区间
```

## 2.13group 分组

```python
# group 分组  
# group()   默认值为 0   返回正则的完整匹配结果
import re
s = 'life is short, i use python'

r = re.search('life.*python', s)
print(r.group())  # life is short, i use python

# () 进行分组
r = re.search('(life.*python)', s)
print(r.group(0))  # life is short, i use python

# group(1)
r = re.search('life(.*)python', s)
print(r.group(1))  #  is short, i use

r = re.findall('life(.*)python', s)
print(r)  #  is short, i use

s = 'life is short, i use python, i love python'
r = re.search('life(.*)python(.*)python', s)
print(r.group(0))  # life is short, i use python, i love python
print(r.group(1))  #  is short, i use
print(r.group(2))  # , i love
print(r.group(0,1,2)) # ('life is short, i use python, i love python', ' is short, i use ', ', i love ')
print(r.groups())  #  (' is short, i use ', ', i love ')

```





### 一些例子

```python
正则表达式

import re

line = 'booooooooobbby123'
r = re.match(".*(b.*b).*", line)
print(r.group(1))       #贪婪模式下，检索到最后符合的内容
print(r.group(0))

r = re.match(".*?(b.*?b).*", line)      #对  ? 后面的 检索进行非贪婪模式
print(r.group(1))  

#  +
print('~+~~~~~~~~~')
r = re.match(".*(b.+b)", line)      #+ 前面内容至少出现一次
print(r.group(1))  


print('|||||')
r = re.match(".*(bbb|bby123)", line)      #  | 或关系 存在一个即可
print(r.group(1))  

print('|||||')
r = re.match(".*(bby123|bbb)", line)      #  | 或关系 存在一个即可
print(r.group(1))

line2 = '15541861937'
regex_str = "(1[2345][0-9]{3})"
r = re.match(regex_str, line2)
print(r.group(0))

#汉字
print('[\u4E00-\u9FA5]+~~~~~~~~~~~~~~~~~~~~~')
line = '你好吗'
r = re.match("[\u4E00-\u9FA5]+", line)
print(r.group(0))

print('[\u4E00-\u9FA5]+~~~~~~~~~~~~~~~~~~~~~')
line = '你  好吗'
r = re.match("[\u4E00-\u9FA5]+", line)
print(r.group(0))

print('[\u4E00-\u9FA5]+~~~~~~~~~~~~~~~~~~~~~')
line = 'study in 北京大学'
r = re.match(".*([\u4E00-\u9FA5]+大学)", line)
print(r.group(1))

print('[\u4E00-\u9FA5]+~~~~~~~~~~~~~~~~~~~~~')
line = 'study in 北京大学'
r = re.match(".*?([\u4E00-\u9FA5]+大学)", line)
print(r.group(1))


line = 'XXX出生于2001年6月'
line = 'XXX出生于2001/6/1'
line = 'XXX出生于2001-6-1'
line = 'XXX出生于2001-06-01'
line = 'XXX出生于2001-06'

regex_str = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))"
```