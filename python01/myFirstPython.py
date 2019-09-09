"""
1.定义变量
 语法：变量名 = 变量值
2.使用变量
3.看变量的特点
"""

# 定义变量：存储数据TOM
my_name = 'TOM'
print(my_name)
# 定义变量
schoolName = '黑马程序员，我唉Python'
print(schoolName)
"""
1.验证数据到底是什么类型
"""
num1 = 1
num2 = 2.2
# int
print(type(num1))
# float
print(type(num2))
# str 单引号和双引号都可以
a = 'hello world'
print(type(a))
b = True
print(type(b))
c = [1, 2, 3, 4]
print(type(c))
# tuple -->元组
d = (1, 2, 3, 4)
print(type(d))
# set --> 集合
e = {1, 2, 3, 4}
print(type(e))
# dict -->字典 （键值对）
f = {'name': 'TOM', 'age': 18}
print(type(f))
