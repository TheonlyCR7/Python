# x, y, z = (1, 2, 3, 4)
# print(x, y, z)
# z, x, y = x, y, z
# print(x, y, z)

# x, *r, y = (1, 2, 3, 4)
# print(x, y)
# print(r)

# stbook = {'name': 'bob', 'age': 12}
# stbook = {'age': 12, 'name': 'bob'}
# key, value = stbook.popitem()
# print(key, value)

# str1 = 'I am a student'
# print(str1.endswith('ent'))
# print(str1.endswith('s'))
# if 0:
#     print("1")
# elif 1:
#     print('2')

# bo = 'a'.lower() < 'B'.lower()
# print(bo)

# a = [1, 2]
# b = [1, 3]
# bo = a > b
# print(bo)

# a = int(input("a = "))
# if a > 10 or a < 0:
# 	print("Great!")
# else:
# 	print("wrong!")

# age = 10
# assert 0 < age < 100
# print('age =', age)
# age *= 10
# assert 0 < age < 100
# print('age =', age)

# age = 24
# assert age < 18, "He is not a boy!"
# AssertionError: He is not a boy!

# name = ''
# while not name:
#     name = input('Please enter your name: ')
# print('Hello, {}!'.format(name))

for num in range(0, 3):
    print(num, end=' ')
