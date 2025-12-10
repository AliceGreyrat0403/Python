# 写文件(write)
# 使用 write 来实现写文件的操作
# f = open('D:\Python_code\python_code\Python基础语法第六篇', 'w')
# f.write('hello')
# f.close()

# 写文件的时候，需要使用 w 的方式打开，如果使用 r 的方式打开，则会抛出异常
# f = open('D:\Python_code\python_code\Python基础语法第六篇', 'r')
# f.write('world')
# f.close()
# 报错：io.UnsupportedOperation（不支持的操作）: not writable（不可写）

# 写方式打开，其实又有两种情况，直接写方式打开，追加方式打开
# f = open('D:\Python_code\python_code\Python基础语法第六篇', 'w')
# f.close()
# # （直接打开关闭）如果使用写方式打开，会清空文件原有的内容！

# f = open('D:\Python_code\python_code\Python基础语法第六篇\code65.txt', 'w')
# f.write('11111\n')
# f.close()
#
# f = open('D:\Python_code\python_code\Python基础语法第六篇\code65.txt', 'a')
# f.write('22222\n')
# f.close()

# 如果文件对象已经被关闭，那么意味着系统中和文件相关的内存资源已经被释放了，强行去写就会出异常
f = open('D:\Python_code\python_code\Python基础语法第六篇/test.txt', 'w')
f.close()
f.write('22222\n')
# 报错：ValueError: I/O operation on closed file.