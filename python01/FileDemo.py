# f = open('test.txt', 'a')  # 访问模式 w a r
# f.write('aaa----->aaaa')
# line = f.readline()
# print(line)
# f.close()
# 访问模式对文件影响

# r+ w+ a+
f = open('test.txt', 'r+')  # w+模式读取，先会清空内容 a+模式读取，指针是在最后读取
content = f.write('111aaaa')
print(content)
f.close()
