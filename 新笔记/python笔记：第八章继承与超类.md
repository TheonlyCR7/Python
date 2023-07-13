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





