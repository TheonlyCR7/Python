# main.py

from module import *


def plus(a, b):
	'''This is a plus'''
	print(a + b)

print(__file__)

import os

module_dir = os.path.dirname(os.path.abspath(__file__))
print(module_dir)

