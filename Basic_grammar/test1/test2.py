d = {
    'name_a' :'Gumby', 'age1':42,
    'name_b' :'bob', 'age2':12,
    'name_c':'lily', 'age3':14}
num = len(d) # 返回字典的键值对数量
print('num=' + str(num))

str1 = d['name_a'] # 参数为键 返回值为对应的值
print('name_a=' + str1)

d['name_a'] = 'tom' # 将tom赋值给name1键
print('name_a=' + d['name_a'])

test = 'name_c' in d # 检查name3键是否在字典中
print(test)

test = 'name_d' in d # 检查name3键是否在字典中
print(test)