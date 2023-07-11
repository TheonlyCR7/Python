与java类似，python作为一种面向对象的编程语言，也可以创建自定义的对象和类。

它的特性主要有：继承，封装，多态，方法，属性，超类



# 1.变量的作用域

  ```python
  c = 50      #全局变量， 作用域为整个模块，若被引用，可作用域整个包
    
  def plus(x,y):
      c = x + y           # 局部变量, 为函数中定义的变量，在函数外可被引用
      print(c)
    
  plus(1,2)
  print(c)                # 函数内部定义的变量只作用与函数内部
  >
  3 
  50
  ```

两者转换

```python
def demo():
    global c        # global  定义一个全局变量，  可被引用 
    c = 2

demo()          
print(c)        # 先调用函数，再输出
> 2
```



# 2.类与构造方法

>   每个类对应每个对象，下面有类变量
>
>   起到封装变量，封装函数，代码的作用

## 2.1定义一个类

格式

```
class 类名:  #首字母最好大写
	代码块
```

```python
class Student:               #命名，首字母大写
    name = '名字'
    age = 0

    def __init__(self):
        #构造函数, 无需调用直接运行  在给对象的赋值语句中即可运行
        print('在创建类对象时先运行构造函数')
        return None     #只能返回none 不可人为指定

    def grape(self, score): # 与java类似，self指向对象本身
        print(self.name + "的成绩是" + str(score))

bob = Student()
> 在创建类对象时先运行构造函数
```

实例化类，给类赋值

```python
student = Student()              #实例化
student.grape(100)             #调用
>
在创建类对象时先运行构造函数
bob的成绩是100
```

## 2.2构造函数

> 在创建对象时，就会被调用运行
>
> 可以没有
>
> 可以在构造函数中， 初始化对象的属性

* 不需要传参的构造函数

```
def __init__(self):
	pass
```

* 需要传参的构造函数，需要有`self`，指向对象，与类无关

```
def __init__(self, name, age):
	pass
```

* 上面两种形式可以同时存在，也可以只存在一种

## 2.3关于self

* self只有在类的方法中才会有，独立的函数或方法是不必带有self的
* self在定义类的方法时是必须有的，但在调用时不必传入相应的参数
* self名称不是必须的，在python中self不是关键词，你可以定义成a或b或其它名字都可以
* self指向对象本身


-   调用构造函数时，可以通过 在类后面（）的方式调用

```python
class Dog:
    def __init__(self):
        print('This is a dog.')

dog()
> This is a dog.
```

调用实例方法时，通过对象调用

```python
class School:               #命名，首字母大写
    name = '未定义'                 
    age = 0                   

    def __init__(self,name1,age1):             
        name = name1
        print(name)                   
        age =  age1                   
        return None     #只能返回none 不可人为指定

#调用构造函数时，通过  在类后面（）的方式调用
#调用实例方法时，通过对象调用
School1 = School(name1 = '中华小学',age1 = '80')
School2 = School(name1 = '安徽小学',age1 = '70')
```

类中函数的实例变量与实参不同

```python
def __init__(self,name1,age1):             
        #可在（）内，  加变量    在引用时，定义变量的值
        #通过 self 来保存特征值
        self.name = name1              
        #通过 self 来定义实例变量和访问实例变量
        self.age =  age1       
        #self.变量属性 = 变量名（形参）
```



## 2.5实例变量与类变量

实例变量：

顾名思义，通过创建对象实例化产生，通过对象进行引用。在类内部表现为：`self.变量名`

类变量：直接与类本身相关，与对象无关，直接在类中被定义，可以转变为实例变量

当出现`对象名.变量名` 引用变量时，先对类里面的实例变量进行寻找，若无，则再去类变量中寻找

```py
class Dog:
	name = 'None' # 类变量
	nickname = 'Name' # 类变量
	def __init__(self, name):  # 这里name为函数形参
		self.name = name  # 赋值实例变量

bob = dog('bobo')
print(bob.name)
print(bob.nickname)
>
bobo
None
```



一个例子

```python
class School():               #命名，首字母大写
    name = '未定义'                 
    age = 0          
    sum = 0                    # 与类相关的变量
    color = 'yellow'
    squire = '面积'

    def __init__(self,name1,age1,color1,squire1):            
        
        name = name1                    
        age =  age1     
        self.color = color1
        self.squire = squire1
        return None     

School1 = School(name1 = '中华小学',age1 = '80',color1 = 'blue',squire1 = '1000')
print(School1.name,'    ', School1.age)     #此时打印出了 类变量 (先在  实例变量  中查找，无， 则到类变量中找)
print(School1.__dict__)                     #以字典的形式输出 School1 的变量
print(School.name)     
print(School1.color,'    ', School1.squire) 
print(School.__dict__)   
```

## 2.4实例方法

格式

```python
def 方法名(self, 形参): # self必须有 形参可有可无
    代码块
```



## 2.5类方法与类变量

类方法的基本格式

```
@classmethod            #为装饰器
def plus_sum(cls):      #cls  为class 的缩写 作用与self类似
    pass
```

类变量：只与类相关

```
__class__.变量名 或者是在类方法中的 cls.变量名   
两者虽然表现形式不同，但为同一变量  `is`
```

下面的例子，很好地通过实例变量与类变量进行班级人数和年龄的统计

```python
class classroom:
sum = 0
    age = 0
    def __init__(self,name,age):
        self.__class__.sum += 1   # 总人数加一
        self.age = age
        self.__class__.age += self.age  # 学生年龄和
        age = self.__class__.age/self.__class__.sum
        print('当前班级学生总人数为:' + str(self.__class__.sum))
        print('当前班级的平均年龄为:' + str(age))

    @classmethod  
    def plus_sum(cls): # 利用类变量进行加和
        print('班级总人数为: ' + str(cls.sum))  

classroom.student1 = classroom(name = '憨批', age = 10)
classroom.student2 = classroom(name = '小逗比', age = 9)  
classroom.student3 = classroom(name = '土豆',age = 8)           
classroom.plus_sum()                # 通过类来调用 方法
classroom.student1.plus_sum()       # 通过对象来调用方法
```

## 2.6静态方法          

-   用的不多   与类 实例方法 关联不大   与普通函数区别不大  

格式：

```
@staticmethod       # 装饰器
def add(x,y):
    print('This is a static method')
```

* 类中的静态方法，可以访问类变量，对于实例变量和其他函数变量，无法访问
* 类中的静态方法，可以通过类直接调用，无需实例化


```python
class Company:
    sum = 0
    bass_name = '刘大钞'
    def __init__(self,staff_a,staff_b,staff_c):
        self.staff_a = staff_a
        self.staff_b = staff_b
        self.staff_c = staff_c
        Company.sum = staff_a + staff_b + staff_c
    
    @staticmethod                   # 装饰器
    def add(x,y):                       # 与类方法实例方法不同，（）内无需强制添加变量
        print('This is a method')
        print(Company.bass_name)        #  正常引用类变量
        print(x + y)                #引用形参
        print(self.staff_a)             #报错
        print(staff_a)                  #报错
    
    Company1 = Company(staff_a = 10,staff_b = 20,staff_c = 30)
    Company1.add(1,2)
    Company.add(1,2)                #可正常被调用
```