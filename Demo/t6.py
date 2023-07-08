# d = {
#     'name_a' :'Gumby', 'age1':42, 
#     'name_b' :'bob', 'age2':12}
# x = d.copy()
# # print(d)
# # print(x)

# # 替换值
# x['name_a'] = 'tom' # 替换副本中的值
# x['age3'] = 54
# del x['age1']
# print(x)
# print(d)

# from copy import deepcopy
# d = {
#     'name_a' :'Gumby', 'age1':42, 
#     'name_b' :'bob', 'age2':12}
# x = deepcopy(d) # 深
# y = d.copy() # 浅
# x.clear()
# print(d)
# print(y)

# d = dict.fromkeys(['name','age'], 'default')
# print(d.get('name', 'N/A'))

# d = {'name_a' :'Gumby', 'age1':42}
# print(d.popitem())
# print(d.popitem())
# print(d)


# d = {'name_a' :'Gumby', 'age1':42}
# d_len = len(d.items())
# print(d_len)
# i = 0
# while(i < d_len):
#     print(d.popitem())
#     i = i + 1

# d = {}
# print(d.setdefault('name', 'None'))
# print(d)

# d1 = {'name': 'bob', 'age': 12}
# d2 = {'name': 'tom'}
# d1.update(d2)
# print(d1)
# {'name': 'tom', 'age': 12}

d1 = {'name': 'bob', 'age': 60, 'weight': 60}
print(d1.values())

