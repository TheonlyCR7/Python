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