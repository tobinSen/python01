# Python math 模块、cmath 模块
import math
import cmath
import time
import calendar

print(math.e)
print(math.fabs(-100))
print(abs(-100))
# print(math.acos(-100))

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4, 5, 6, 7]
# print(cmp(list1, list2))
tup2 = (1, 2, 3, 4, 5, 6, 7)
# print(tup2[1:4])
print(time.time())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(calendar.month(2018, 5))
