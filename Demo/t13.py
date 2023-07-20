# import sys
# sys.path.append('D:\M\github\Python\Demo\hello.py') 

import hello
hello.hello1()
print(hello.__name__)

import box
import box.shapes as sh
print(dir(sh))
print(sh.__all__)