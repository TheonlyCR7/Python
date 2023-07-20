# 1.系统函数

由系统提供，直接拿来用或是导入模块后使用

```
a = 1.12386
result = round(a,2)
print(result)
> 1.12
```



# 2.自定义函数

* 函数是结构化编程的核心
* 使用关键词`def`来定义函数

```
#函数定义
def funcname(parameter_list):
    pass
#1.参数列表可以没有
#2.用 return 返回值value， 若无return 语句，则返回none; 函数内部遇到 return 则停止运行
```

```python
def add(x,y):
    result = x + y
    return result

#定义函数时，不可与系统函数同名
def print_code(code):
    print(code)
```

```python
def hello(name):
	return 'Hello, {}!'.format(name)
```

```python
def hello(name):
	return 'Hello, {}!'.format(name)
str1 = input('name = ')
print(hello(str1))
>
name = lmc
Hello, lmc!
```

* 为函数添加文档字符串

```python
def hello(name):
	'Welcome for users'  # 文档字符串
	return 'Hello, {}!'.format(name)
print(hello.__doc__)
> 'Welcome for users' 
```

## 2.1 函数的返回值

* 如果不自定义返回值，则无返回值
* 关键字 `return`

```python
def test():
	print('hello')
	return 
	print('end')
test()
> hello
```

* 用明确的变量组来接受函数输出值，便于后期查看（序列解包），不用元组

```python
def damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2

skill1_damage, skill2_damage = damage(3,6)
print(skill1_damage,skill2_damage)
> 9 22
```

* 标明函数的返回值

```
def printer() -> int:  # 标明返回值为int型
    return 11
```

```
# Exception的构造函数
class Exception(BaseException):
	# 通过 -> None表明函数没有返回值
    def __init__(self, *args: object) -> None:
        pass
```

注意：这里只起到标明作用，运行过程中不会影响返回值

```python
def printer() -> str:  # 标明返回值为str
    return 11  # 实际上为int
a = printer()
print(type(a))
>
<class 'int'>  
```



## 2.1 函数的参数

* 指定赋值调用，增加可读性

```python
def add(x,y):
    result = x + y
    return result
c = add(y=3,x=2)  # 指定赋值，与顺序无关，可读性
print(c)
> 5
```

* 给函数设置默认参数，不传参也能可以调用

```python
# collage已经设置默认参数，不传参即采用默认参数
def print_files(name,age,gender,collage='liaoning University'):
    print('My name is ' + name)
    print('I am ' + age)
    print('My gender is ' + gender)
    print('My school is '+ collage)

print_files('阿衰',str(18),'man')
>
My name is 阿衰
I am 18
My gender is man
My school is liaoning University   # 默认参数

print_files('阿衰',str(18),'man', '怕跌中学')
> 
My name is 阿衰
I am 18
My gender is man
My school is 怕跌中学
```

* 星号参数 类似于序列解包中的星号变量 接收余下位置的参数（或全部接收）

```python
def printer(*ele):
    print(ele)
    
d = 11
printer(d)
> (11,)  # 输出的为元组  
```

> 这里必须有逗号才能是元组  无逗号`(11)` 类型为int

```python
a = (11,)
b = (11)
print(type(a))
print(type(b))
> 
<class 'tuple'>
<class 'int'>
```

* 利用*星号接收更多数据

```python
def printer(a, b, *ele):
    return ele
    
tuple1 = printer(1,2,3,4,5)
print(tuple1)
> (3, 4, 5)
```

```python
def printer(a, b, *ele):
    print(ele)
    
tuple1 = (1,2,3,4,5)
printer(*tuple1)
> (3, 4, 5)
```

* 双星号传递字典

```python
def hello(greeting = 'Hello', name = 'world'):
	print('{}, {}!'.format(greeting, name))
params = {'name': 'bobo', 'greeting': 'well met'}
print()
```

* 对于星号的使用，能不用最好，一般情况下，也可以达到相同效果
* 多用于：
  * 定义的函数，允许可变数量的参数
  * 调用函数时，拆分字典或序列使用





