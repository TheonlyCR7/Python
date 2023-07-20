# def printer() -> str:
#     return 11
# a = printer()
# print(type(a))


# class CustomException(Exception):
#     def __init__(self, message):
#         super().__init__(message) # 与上个程序第五行同理

# # 若出现异常，则要求用户重新输入
# while True:
#     try:
#         # 获取用户输入的除数和被除数
#         divisor = int(input("Enter the divisor: "))
#         dividend = int(input("Enter the dividend: "))
#         result = dividend / divisor
#     # 通过元组进行多种异常监测
#     except Exception as ex:
#         # 捕获多种异常
#         print(ex)
#     else:
#         print(f"The result of division is: {result}")
#         break  # 成功即跳出循环

# def divide(x, y):
#     return x / y

# # 测试
# try:
#     result = divide(6, 0)
# # 接收异常
# except Exception as ex:
#     print(f"Error: {str(ex)}")
# else:
#     print(result)

# class Celsius:
#     def __init__(self, temperature=0):
#         self._temperature = temperature

#     def to_fahrenheit(self):
#         return (self._temperature * 1.8) + 32

#     def get_temperature(self):
#         print("Getting value...")
#         return self._temperature

#     def set_temperature(self, value):
#         print("Setting value...")
#         self._temperature = value

#     temperature = property(get_temperature, set_temperature)

# c = Celsius()
# print(c.temperature)
# c.temperature = -1
# print(c.temperature)
# c.temperature = 10
# print(c.temperature)


class MyIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
        
try:
    my = MyIterable()
except StopIteration as se:
    print(str(se))


