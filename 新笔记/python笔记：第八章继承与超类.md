与java类似，继承的出现是为了提高代码的重复利用率，避免多次输入同样的代码。而超类就是java中的父类。

# 1.继承

要指定超类，可在定义类时，在class语句中的类名后加上超类名

* 基类就是超类，派生类就是子类

格式

```
class Dog:   # 
	pass

class Bobo(Dog):  # Dog类的子类
	pass
```

子类会

* 重新定义重写超类方法init
* 继承超类的方法，无需再次编写

```python
class Dog:
    def __init__(self):
        print('wang!!!')
    
    def eat(self):
        print('Dog is eating.')
    
class Bobo(Dog):  # 继承Dog
    pass

tom = Bobo()
tom.eat()
> 
wang!!!
Dog is eating.
```

在子类中进行重写

```python
class Dog:
    def __init__(self):
        print('wang!!!')
    
    def eat(self):
        print('Dog is eating.')
    
class Bobo(Dog):
    def __init__(self):
        print('Bobo is wang!')

    def eat(self):
        print('Bobo is eating.')

tom = Bobo()
tom.eat()
>
Bobo is wang!
Bobo is eating.
```



## 1.1查找一个类的子类和基类

* `issubclass` 确定一个类是否是另一个类的子类

```
issubclass(Bobo, Dog)  # 子类 超类
> True
issubclass(Dog, Bobo)
> False
```

* 已知一个类，想知道它的基类，访问特殊属性 `__bases__`

```python
print(Bobo.__bases__)
> (<class '__main__.Dog'>,)
```

* `isinstance` 确定创建的对象是否是特定类的实例

  创建子类的实例，这个对象同时也是其基类的实例

```python
class Dog:
    pass
    
class Bobo(Dog):
    pass

tom = Bobo()

print(isinstance(tom, Bobo))
print(isinstance(tom, Dog))
>
True
True
```

* 使用属性`__class__` 可以知道该实例属于哪个类

```python
print(tom.__class__)
> <class '__main__.Bobo'>
```



## 1.2 多个超类

尽量避免使用

格式

```python
class A:
	pass
class B:
	pass

class C(A, B):  # 同时继承A和B
	pass 
```



## 1.3接口

接口这一概念与多态相关。实际上，python中没有与java相对应的接口。需要特定的模块来实现



## 1.4 抽象基类

抽象类不能（不应该）被实例化，用于定义子类应该实现的一些抽象方法。

格式

```python
from abc import ABC, abstractmethod
class 类名(ABC):  # 继承ABC类
	@abstractmethod   # 标记为抽象方法，在子类中必须实现
	def 方法名(self):
		pass
```

```python
from abc import ABC, abstractmethod

class Dog(ABC):
    @abstractmethod
    def eat(self):
        pass
    
class Bobo(Dog):
    def eat(self):
        print('eating.')

tom = Bobo()
tom.eat()
> eating.
```

## 1.5 重写

重写是继承的重要方面

```python
class Dog:
	def eat(self):
		print('Dog is eating')

class Bobo(Dog):
	def eat(self):
		print('Bobo is eating')
		
bobo = Bobo()
bobo.eat()
> Bobo is eating
```



# 2. 子类对超类的访问

## 2.1调用超类构造函数

通过函数super

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print("I'm an animal. My name is", self.name)

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name) # super调用超类构造函数 并传递参数
        self.age = age
        print("My name is", self.name, "and I'm", self.age, "years old.")

my_dog = Dog("Buddy", 3)
```

运行结果

```
I'm an animal. My name is Buddy
My name is Buddy and I'm 3 years old.
```



# 3.一些魔法方法

## 3.1 函数property

`property` 是一个内置的 Python 函数，它可以将类方法转换为属性。

使用 `property` 可以让我们通过类方法对属性进行访问和修改，而**无需直接访问属性**。这样可以帮助我们更好地控制属性的访问方式和值。它通常用于**封装类的属性**。

```
property(fget=None, fset=None, fdel=None, doc=None)
其中：
fget：获取属性值的方法（getter）
fset：设置属性值的方法（setter）
fdel：删除属性值的方法（deleter）
doc：属性文档字符串
```

其中 `fget` 是必须的，而 `fset` 和 `fdel` 可选。

如果只需要实现只读属性，则只需定义 `fget` 方法。

如果需要定义可写属性，则需要定义 `fget` 和 `fset` 方法。

一个例子：

```
class Celsius:
    def __init__(self, temperature=0):  # 默认值为0
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    def get_temperature(self): # 获取值
        print("Getting value...")
        return self._temperature

    def set_temperature(self, value): # 修改值
        print("Setting value...")
        self._temperature = value

	# 进行方法聚合
    temperature = property(get_temperature, set_temperature)

c = Celsius()  # 创建实例
print(c.temperature)
c.temperature = 37
print(c.temperature)
c.temperature = 10
print(c.temperature)
```

运行结果

```
Getting value...
0
Setting value...
Getting value...
-1
Setting value...
Getting value...
10
```



## 3.2 迭代器

