# 关闭文件

# 打开文件个数的上限

flist = []
count = 0
while True:
    f = open('D:\Python_code\python_code\Python基础语法第六篇\code61.py', 'r')
    flist.append(f) # Python留的一个后手
    count += 1
    print(f'打开文件的个数: {count}')
# 光是打开没有关闭，报错：OSError: [Errno 24] Too many open files: ......
f.close(f)
# 在系统中，是可以通过一些设置项，来配置能打开文件的最大数目的
# 但是无论配置多少，都不是无穷无尽的~~就需要记得要及时关闭，释放资源