# 矩形
i = 0
while i < 5:
    j = 0
    while j < 5:
        print('*', end='')
        j += 1
    print()
    i += 1
# 三角形
i = 0
while i < 5:
    j = 0
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1
# 99乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f'{i} * {j} = {i * j}', end='\t')
        j += 1
    print()
    i += 1

for i in 10, 12, 2:
    print(i)
for i in 'ithema':
    if i == 'e':
        break
    print(i)
z = 0
while z < 5:
    print(z)
    z += 1
else:
    print('zzz')

for i in 1, 2, 3, 4, 5:
    print(i)
    if i == 3:
        continue
else:
    print(i)

f = 'I\'m TOM'

str1 = 'abcdef'
print(str1[0])
print(str1[1])
print(str1[2])

name = 'abcdefg'
print(name[2:5:3])

str2 = '0123456789'
print(str2[2:5:1])  # 234
print(str2[2:5:2])  # 24
print(str2[2:5])  # 234
print(str2[2:])  # 23456789
print(str2[:5])  # 01234
print(str2[::-1])  # 9876543210
print(str2[-4:-1])  # 678 步长为负数，表示倒叙选取

print(str2[-4:-1:1])  # 678
print(str2[-4:-1:-1])  # 不能选取出数据 如果选取的方向和步长的方向不同，则无法选取
print(str2[-1:-4:-1])  # 987

str3 = 'abcdefgh'
print(str3[1:4:-1])
print(str3[1:4:1])

# str3[:3] = '123'
# print(str3)

var1 = 'Hello World!'

print('更新字符串 :- ', var1[:6] + 'Runoob!')
