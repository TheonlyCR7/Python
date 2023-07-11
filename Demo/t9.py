# a = 1.12386
# result = round(a,2)
# print(result)

# def hello(name):
# 	'Welcome for users'
# 	return 'Hello, {}!'.format(name)
# print(hello.__doc__)

# def print_files(name,age,gender,collage='liaoning University'):
#     print('My name is ' + name)
#     print('I am ' + age)
#     print('My gender is ' + gender)
#     print('My school is '+ collage)

# print_files('阿衰',str(18),'man')
# print_files('阿衰',str(18),'man', '怕跌中学')

# def printer(a, b, *ele):
#     print(ele)
#     return ele

# d = 11
# b = printer(d)
# a = (11)
# print(type(a))
# print(type(b))
# if a == b: print('y')

# def printer(**ele):
#     return ele

# tuple1 = printer(1,2,3,4,5)
# print(type(tuple1))

def printer(a, b, *ele):
    print(ele)
    
tuple1 = (1,2,3,4,5)
printer(*tuple1)