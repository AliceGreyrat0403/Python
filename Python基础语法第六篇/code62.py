# 文件操作
# 打开文件

# 使用 open 打开一个文件
# f = open('d:/Python/test.txt', "r")
# 报错：FileNotFoundError: [Errno 2] No such file or directory: 'd:/Python/test.txt'
f = open('D:\Python_code\python_code\Python基础语法第六篇\code61.py', "r")
print(f)
print(type(f))
# 运行结果如下所示——>
# <_io.TextIOWrapper name='D:\\Python_code\\python_code\\Python基础语法第六篇\\code61.py' mode='r' encoding='cp936'>
# <class '_io.TextIOWrapper'>

# 文件打开了是一定要关闭的
f.close()