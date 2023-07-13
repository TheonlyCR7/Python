# 1.1 异常是什么

python使用异常对象来表示异常状态，并在遇到错误时引发异常。异常对象未被处理，程序将终止并显示一条错误信息。

我们可以通过各种方法引发和捕获错误，并采取对应措施。



# 1.2 将“错误”变成异常

自主地引发异常

## 1.2.1 raise语句

我们通过预测异常可能发生的位置，通过raise语句主动抛出异常，用except语句来接收前面出现的异常，并作出对应的操作

```python
def divide(x, y):
    if y == 0:
    	# 引出异常
        raise ZeroDivisionError("Division by zero!")
    else:
        return x / y

# 测试
try:
    result = divide(6, 0)
# 接收异常
except ZeroDivisionError as ex:
    print(f"Error: {str(ex)}")
else:
    print(result)
> Error: Division by zero!
```

一些常见的内置异常类

```
Exception   # 几乎所有异常类均由这个派生而来
AttributeError	试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError	输入/输出异常；基本上是无法打开文件
ImportError	无法引入模块或包；基本上是路径问题或名称错误
IndentationError	语法错误（的子类） ；代码没有正确对齐
IndexError	下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError	试图访问字典里不存在的键
KeyboardInterrupt	Ctrl+C被按下
NameError	使用一个还未被赋予对象的变量
SyntaxError	Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError	传入对象类型与要求的不符合
```




# 1.3 自定义的异常类

首先，要直接或间接地继承`Exception`类

格式

```python
class 异常类名(Exception):
	pass
```

利用自定义的异常类对1.2中的例子进行改进

```python
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
```

## 1.3.1一个具体使用场景

检查用户输入的邮件格式，不对则报错

```python
class InvalidEmailException(Exception):
    def __init__(self, email):
        self.email = email
        self.message = f"{email} is not a valid email address. Please try again."
        super().__init__(self.message)

def send_email(to, subject, body):
    if "@" not in to:
        raise InvalidEmailException(to)  # 抛出异常
    print(f"Email sent to {to} with subject '{subject}' and body '{body}'.")

# 测试
try:
    send_email("invalid-email", "Test email", "This is a test email.")
except InvalidEmailException as ex:
    print(f"Error: {ex.message}")
```

第五行`super().__init__(self.message)` 调用基类 `Exception` 的构造函数来初始化 `self.message`。

Exception的构造函数：

```python
class Exception(BaseException):
    def __init__(self, *args: object) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        pass
```

构造函数接受可变长度的参数 `*args`，但是它并没有执行任何实际操作，只是一个空的 `pass` 语句。这意味着，我们可以在自定义异常类的构造函数中调用父类 `Exception` 的构造函数，同时传递自定义的错误消息作为参数。



关于第五行的作用：

* 第5行的作用只是使用基类 `Exception` 的构造函数，来完成可能会影响异常的某些其他行为，如设置异常的堆栈跟踪信息等。这些信息可以帮助程序员更轻松地找到代码中发生异常的位置。

  因此，虽然第5行实际上不是非常必要，但它是一个良好的实践，可以帮助进一步丰富异常信息。

* 个人认为，可以通过重写Exception的构造函数

* 猜想：可能会定义多个自定义类，通过定义Exception参数的方式，进行类之间的异常信息传递



### 1.3.2 同时监测多种异常

将异常类型以元组形式展现（没有采用raise，等待程序抛出异常并接收）

```python
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message) # 与上个程序第五行同理

# 若出现异常，则要求用户重新输入
while True:
    try:
        # 获取用户输入的除数和被除数
        divisor = int(input("Enter the divisor: "))
        dividend = int(input("Enter the dividend: "))
        result = dividend / divisor
    # 通过元组进行多种异常监测
    except (ZeroDivisionError, TypeError, ValueError) as ex:
        # 捕获多种异常
        print(ex)
    else:
        print(f"The result of division is: {result}")
        break  # 成功即跳出循环
```

运行结果

```python
Enter the divisor: 0
Enter the dividend: 1
division by zero
Enter the divisor: we
invalid literal for int() with base 10: 'we'
Enter the divisor: 2
Enter the dividend: 1
The result of division is: 0.5
```

### 1.3.3 一网打尽的异常和else

同时监测多个异常可能不够，可以一网打尽

```python
# 若出现异常，则要求用户重新输入
while True:
    try:
        # 获取用户输入的除数和被除数
        divisor = int(input("Enter the divisor: "))
        dividend = int(input("Enter the dividend: "))
        result = dividend / divisor
    # 通过元组进行多种异常监测
    except Exception as ex:   
    #对所有Exception的子类异常进行监测，只有发生了对应的子类异常，才会被捕获
        # 捕获多种异常
        print(ex)
    else:  # 通过else语句实现循环，这里是except语句的else, 当不执行except语句时，执行else
        print(f"The result of division is: {result}")
        break  # 成功即跳出循环
```

运行结果

```
Enter the divisor: er
invalid literal for int() with base 10: 'er'
Enter the divisor: 0
Enter the dividend: 1
division by zero
Enter the divisor: 1
Enter the dividend: 2
The result of division is: 2.0
```

**tip:**

> 在编写代码时，最好不要捕获所有异常类型。我们应该尽可能地特定地捕获那些预期的、已知的异常类型，并将其他异常类型传递给更高层的异常处理机制进行处理。这样可以更加有效地调试和解决问题，而且代码更加可读和可维护。



### 1.3.4 最后的finally

无论是否发生异常，finally语句均会运行。多用于执行清理工作。

如：关闭文件，关闭网络套接字等

```
try:
    1 / 2
except NameError:
    print("Unknown wariable")
else:
    print('That went well')
finally:
    print('Cleaning up.')
```

运行结果

```python
That went well
Cleaning up.
```



### 1.3.5 异常的传递

如果不处理函数中引发的异常，它将向上传播到调用函数中，直到主程序，若主程序中还是不能处理异常，程序将通知并显示站跟踪信息。

```python
def faulty():
    raise Exception("wrong")

def ig_exception():
    faulty()

def hl_exception():
    try:
        faulty()
    except:
        print('Exception handled')
ig_exception()
```

运行结果：打印了栈跟踪信息和异常信息

```
Traceback (most recent call last):
  File "d:\M\github\Python\Demo\t12.py", line 12, in <module>
    ig_exception()
  File "d:\M\github\Python\Demo\t12.py", line 5, in ig_exception
    faulty()
  File "d:\M\github\Python\Demo\t12.py", line 2, in faulty
    raise Exception("wrong")
Exception: wrong
```

若是只调用`hl_exception()` 异常会被处理，程序不会终止

```python
hl_exception()
print("hello")  # 打印出结果，说明程序未终止，仍在运行
> Exception handled
> hello
```



## 1.4 异常之禅

* 除了使用try/except语句来处理异常外，还可以使用if/else语句，只是不推荐这样做
* 可以检查对象是否包含特定的属性

```python
try:
	obj.write
except AttributeError:
	print('The object is not worteable')
else:
	print('The object is writeable')
```

* 不那么异常的时候，可以发出警告，由模块`warning` 中的函数warn提供

```python
from warnings import warn
warn('got a bad feeling.')
print('hello')   # 可以打印，说明程序仍在运行
> 
d:\M\github\Python\Demo\t12.py:2: UserWarning: got a bad feeling.
  warn('got a bad feeling.')
hello
```

