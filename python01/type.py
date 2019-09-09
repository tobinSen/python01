age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
# 1.今年我的年龄x岁
print('今年我的年龄是%d岁' % age)
# 2.我的名字是x
print('我的名字是%s' % name)
# 3.我的体重是x公斤 （保留几位小数 %.2f）
print('我的体重是%.2f公斤' % weight)
# 4.我的学号是x
print('我的学号是%03d' % stu_id)
# 5.我的名字是x，今年x岁了
print('我的名字是%s,今年%d岁了' % (name, age))
print('我的名字是%s,明年%d岁了' % (name, age + 1))
# 6.我的名字是x,今年x岁了，体重x公斤，学号是x
print('我的名字是%s,今年%d岁了，体重%0.2f公斤，学号是%03d' % (name, age, weight, stu_id))
# 7.我的名字是x，今年x岁了，体重x公斤
print('我的名字是%s，今年%s岁了，体重%s公斤' % (name, age, weight))
# 语法 f'{表达式}'
print(f'我的名字是{name},今年{age + 1}岁了')

# 转义字符
print('hello\nworld')
print('hello\tworld')

# end = '\n'
print('hello', end='\n')
print('world', end='\t')
print('world', end='...')

# input('提示信息')
# password = input("请输入一个数字：")
# print(f'您输入的密码是{password}')

# 数据类型转换
# password = input("请输入一个数字：")
# print(type(password))  # str
# print(type(int(password)))  # int
# print(f'您输入的密码是{password}')
# print(type(float(password)))
# print(float(password))
# str(password)

list1 = [1, 2, 3, 4]
print(tuple(list1))

tuple1 = (1, 2, 3, 4)
print(list(tuple1))

# eval()
str1 = '1'
str2 = '1.1'
str3 = '(12,13,14)'
str4 = '[15,16,17]'
print(type(eval(str1)))
print(eval(str1))
print(type(eval(str2)))
print(eval(str2))
print(type(eval(str3)))
print(eval(str3))
print(type(eval(str4)))
print(eval(str4))
