class MyException(Exception):  # 自定义异常类
    pass

def divide(x, y):
    if y == 0:
        raise MyException("Division by zero!")
    else:
        return x / y

# 测试
try:
    result = divide(6, 0)
except MyException as ex:
    print(f"Error: {str(ex)}")
else:
    print(result)