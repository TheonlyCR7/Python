from warnings import warn
warn('got a bad feeling.')
print('hello')


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


