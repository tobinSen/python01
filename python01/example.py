# 6大功能：1.增 2，删 3，改 4，查

global_list = []


def add_info(**kwargs):
    """
    添加人员信息
    :param kwargs: 格式：add(name=add_name, age=add_age, gender=add_gender)
    :return: True:添加成功，False：添加失败
    """
    add_name = kwargs['name']
    add_age = kwargs['age']
    add_gender = kwargs['gender']
    dict = {'name': add_name, 'age': add_age, 'gender': add_gender}
    global global_list
    for i in global_list:
        if i['name'] == add_name:
            return False
    global_list.append(dict)  # 不能转换，转换会产生一个新的列表
    return True


def del_info(*args):
    """
    删除人员信息
    :param args: ([tongjian,tongjian],)
    :return:
    """
    unDel_list = []
    global global_list
    for i in args[0]:
        for dict in global_list:
            if dict['name'] == i:
                global_list.remove(dict)
            else:
                unDel_list.append(i)
    else:
        return unDel_list, True if len(global_list) == 0 else False


def update_info(**kwargs):
    """
    更新页面
    :param kwargs:
    :return:
    """
    global global_list
    update_name = kwargs['name']
    update_age = kwargs['age']
    update_gender = kwargs['gender']

    for i in global_list:
        if i['name'] == update_name:
            i['age'] = update_age
            i['gender'] = update_gender
            return True
    else:
        return False


def search_info(name):
    """
    查询个人信息
    :param name:
    :return:
    """
    global global_list
    for i in global_list:
        if name == i['name']:
            return i
    else:
        return {}


def search_all():
    global global_list
    return global_list


while True:
    opt = input('请输入选项(1-6):\n'
                '1.增加数据\n'
                '2.删除数据\n'
                '3.更新数据\n'
                '4.查询数据\n'
                '5.查询所有\n'
                '6.退出系统\n')
    if opt.isdigit():
        opt = int(opt)
    else:
        print('请输入数字...')

    if opt == 1:
        add_name = input('请输入姓名:\n')
        if add_name == '': print('姓名不能为空!!!')
        add_age = input('请输入年龄:\n')
        if add_age == '': print('年龄不能为空!!!')
        add_gender = input('请输入性别:\n')
        if add_gender == '': print('性别不能为空!!!')
        isSuccess = add_info(name=add_name, age=add_age, gender=add_gender)
        print(f'添加成功，姓名：{add_name}，年龄：{add_age},性别：{add_gender}') if isSuccess else print(f'姓名{add_name}已经存在，无法添加...')
    elif opt == 2:
        del_names = input('请输入删除的姓名：\n')
        if del_names == '': print('删除姓名不能为空!!!')
        list = del_info(tuple(del_names.split(',')))
        if len(list[0]) == 0:
            print("删除成功...")
        elif list[1]:
            print('系统为空，无法删除...')
        else:
            print(f'{list[0]}不能进行删除')
    elif opt == 3:
        update_name = input('请输入姓名：\n')
        update_age = input('请输入年龄：\n')
        update_gender = input('请输入性别：\n')
        isSuccess = update_info(name=update_name, age=update_age, gender=update_gender)
        print('更新成功') if isSuccess else print('更新失败')
    elif opt == 4:
        search_name = input('请输入姓名：\n')
        print(search_info(search_name))
    elif opt == 5:
        print(search_all())
    elif opt == 6:
        break
    else:
        print('输入的选项有误，请从新选择...\t')
