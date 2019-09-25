class A(object):
    print_num = 11

    def __init__(self):
        self.num = 1
        print('A的__init__初始化')

    def info_print(self):
        print(self.num)


class C(object):
    print_num = 12

    def __init__(self):
        self.num = 2
        print('C的__init__初始化')

    def info_print(self):
        print(self.num)


class B(C, A):  # 这里重写也是默认重写第一个父类的方法 ,只会初始化第一个父类的__init__方法

    def __init__(self):
        self.num = 3

    def info_print(self):
        super(B, self).__init__()

        A.__init__(self)
        A.info_print(self)

        C.__init__(self)
        C.info_print(self)

        print('不会打印...')


b = B()
print(b.print_num)
b.info_print()
print(B.mro())
