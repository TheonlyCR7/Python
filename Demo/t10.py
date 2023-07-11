# c = 50      #全局变量， 作用域为整个模块，若被引用，可作用域整个包
  
# def plus(x,y):
#       c = x + y           # 局部变量, 为函数中定义的变量，在函数外可被引用
#       print(c)
  
# plus(1,2)
# print(c)                # 函数内部定义的变量只作用与函数内部

# print('~~~~~~~例子~~~~~~~')
  
# def demo():
#     a = 10
# #print(a)                #会 显示为 a 未被定义

# class Student():               #命名，首字母大写
#     name = '名字'
#     age = 0

#     def __init__(self):
#         #构造函数, 无需调用直接运行    在给对象的赋值语句中即可运行
#         print('在创建类对象时先运行构造函数')
#         return None     #只能返回none 不可人为指定
    
#     def grape(self,score):
#         print(self.name + "的成绩是" + str(score))

# bob = Student()
# bob.name = 'bob'
# bob.grape(100)

# class School():               #命名，首字母大写
#     name = '未定义'                 
#     age = 0                   

#     def __init__(self,name1,age1):             
#     #可在（）内，  加变量    在引用时，定义变量的值
#     #在构造函数中， 初始化对象的属性  （此函数中初始化 name age）
#         self.name = name1
#         print(self.name)                   
#         age =  age1                   
#         return None     #只能返回none 不可人为指定

# #调用构造函数时，通过  在类后面（）的方式调用
# #调用实例方法时，通过对象调用
# ZH = School(name1 = '中华小学',age1 = '80')
# LN = School(name1 = '安徽小学',age1 = '70')
# print(ZH.name)               


# class dog():
#     name = 'none'

#     def __init__(self):
#         print('This is a dog.')

#     # def __init__(self, name1):
#     #     name = name1

# dog()

# class School():               #命名，首字母大写
#     name = '未定义'                 
#     age = 0          
#     sum = 0                    # 与类相关的变量
#     color = 'yellow'
#     squire = '面积'

#     def __init__(self, name1, age1, color1, squire1):            
        
#         name = name1                    
#         age =  age1     
#         self.color = color1
#         self.squire = squire1
#         return None     

# School1 = School(name1 = '中华小学',age1 = '80',color1 = 'blue',squire1 = '1000')
# print(School1.name,'    ', School1.age)     #此时打印出了 类变量 (先在  实例变量  中查找，无， 则到类变量中找)
# print(School1.__dict__)                     #以字典的形式输出 School1 的变量
# print(School.name)     
# print(School1.color,'    ', School1.squire) 
# print(School.__dict__)   

# class dog:
# 	name = 'None'
# 	nickname = 'None'
# 	def __init__(self, name):
# 		self.name = name
		
# 	def fun(self):
# 		print('eating')
# 		return 'look'

# bob = dog('bobo')
# bob.fun()


# class classroom:
#     sum = 0
#     age = 0
#     def __init__(self,name,age):
#         self.__class__.sum += 1
#         self.age = age
#         __class__.age += self.age
#         age = self.__class__.age/__class__.sum
#         print('当前班级学生总人数为:' + str(self.__class__.sum))
#         print('当前班级的平均年龄为:' + str(age))

#     # 定义一个    类方法
#     @classmethod            #为装饰器
#     def plus_sum(cls):      #cls  为class 的缩写   名字不唯一   也可为 self
#         print('班级总人数为: ' + str(cls.sum))
    
#     def printer(self):
#         print('__class__.sum =', __class__.sum)
#         print('self.age =', self.age)

# student1 = classroom(name = '憨批', age = 10)
# student2 = classroom(name = '小逗比', age = 9)  
# student3 = classroom(name = '土豆',age = 8)           
# classroom.plus_sum()                # 通过类来调用 方法
# # student1.plus_sum()       # 通过对象来调用方法

# student1.printer()

# class Dog:
#     def __init__(self):
#         print('构造函数')

#     @classmethod
#     def clsmethod(cls):
#         print('类方法')

# bob = Dog()

# @staticmethod       # 装饰器
# def add(x,y):
#     print('This is a static method')
class Company:
    sum = 0
    bass_name = '刘大钞'
    def __init__(self,staff_a,staff_b,staff_c):
        self.staff_a = staff_a
        self.staff_b = staff_b
        self.staff_c = staff_c
        Company.sum = staff_a + staff_b + staff_c
        print(Company.sum)
    
    @staticmethod                   # 装饰器
    def add(x,y):                       # 与类方法实例方法不同，（）内无需强制添加变量
        print('This is a method')
        print(Company.bass_name)        #  正常引用类变量
        print(x + y)                #引用形参
        # print(self.staff_a)             #报错
        # print(staff_a)                  #报错
    
Company1 = Company(staff_a = 10,staff_b = 20,staff_c = 30)
Company1.add(1,2)
Company.add(1,2)                #可正常被调用




