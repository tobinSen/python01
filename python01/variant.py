# 方式一：
a1 = 1
a2 = 2
# 方式二：
a3 = a4 = a5 = 3
# 方式三
a, b, c = 1, 2, "john"
# 删除引用
del a
print(f'a:{b},b:{b},c:{c}')
c = 10
c += 1 + 1
print(c)
d = 10
d = True
d *= 1 + 2
print(d)

print((a < b) and (c < b))
