# f = open('test.txt', 'w')
# f.write('Hello')
# f.close

# f = open('test.txt', 'r')
# str1 = f.read(4)
# print(str1)
# f.seek(0)
# str1 = f.read()
# print(str1)

# f = open('test.txt', 'r')
# str1 = f.readlines()
# print(str1)
# f.close

# f = open('test.txt', 'w')
# f.write('middle')
# f.writelines('bad\n')
# f.writelines('good')
# f.close

# try:
#     f = open('test.txt', 'w')
#     f.write('middle')
#     f.writelines('bad\n')
#     f.writelines('good')
# finally:
#     f.close



# with open('test.txt', 'r') as f:
#     str = f.read()
#     print(str, end=' ')

import fileinput

counts = {}

# 逐行读取文件并统计
for line in fileinput.input('test.txt'):
    key = line.strip()
    counts[key] = counts.get(key, 0) + 1

# 输出统计结果
for key, value in counts.items():
    print(key, '--', value)

