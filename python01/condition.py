# python 严格遵循缩进关系
if True:
    print('True的执行语句')

age = 20
if age > 18:
    print('可以上网')
print('系统关闭')

user_age = input('输入你年龄')  # input输入的都是字符串
if int(user_age) > 18:
    print(f'可以上网{user_age}')
else:
    print(f'不能上网{user_age}')

user_phone = int(input('电话号码：'))
if (user_phone > 10) and (user_phone < 20):
    print(f'{user_phone}if案例')
elif (user_phone > 20) and (user_phone < 30):
    print(f'{user_phone}elif的案例')
else:
    print(f'{user_phone}else')

if 10 < user_phone < 20:
    print(f'{user_phone}if案例')
elif 20 < user_phone < 30:
    print(f'{user_phone}elif的案例')
else:
    print(f'{user_phone}else')

if 10 < user_phone:
    if 20 > user_phone:
        print(f'{user_phone}if嵌套')
    else:
        print('else')
else:
    print('条件')
