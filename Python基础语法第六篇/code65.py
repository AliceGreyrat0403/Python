# 读文件

# 1、使用 read 来读取文件内容，指定读几个字符。
f = open('D:/Python_code/python_code/Python基础语法第六篇/test.txt', 'r')
result = f.read(2)
print(result)
f.close()
# 报错：UnicodeDecodeError: 'gbk' codec can't decode byte 0x89 in position 14: illegal multibyte sequence
# 中文和英文类似，在计算机中，都是使用“数字”来表示字符的
# 哪个数字，对应哪个汉字？其实在计算机中，可以有多个版本
# 最主流的版本：（1）GBK；（2）UTF8。
# 这里是UTF-8的格式：此处我们使用的办法，是让代码按照UTF-8来进行处理
# 相比于gbk，UTF-8是使用更广泛的编码方式（最最主流的写法）
# f = open('D:/Python_code/python_code/Python基础语法第六篇/test.txt','r',encoding='utf8')
# result = f.read(2)
# print(result)
# f.close()

# 2、更常见的需求，是按行来读取
# 最简单的办法，直接 for 循环
# f = open('D:/Python_code/python_code/Python基础语法第六篇/test.txt','r',encoding='utf8')
# for line in f:
#     print(f'line = {line}')
# f.close()

# 读出来的结果多了个空行
# line = 床前明月光
#
# line = 疑是地上霜
#
# line = 举头望明月
#
# line = 低头思故乡
# 之所以多了个空行，是因为本来读到的文件内容（这一行内容，末尾就带有\n）
# 此处使用print来打印，又会自动加一个换行符
# 解决方案：可以给print再多设定个参数，修改print自动添加换行的行为

# 实操
# f = open('D:/Python_code/python_code/Python基础语法第六篇/test.txt','r',encoding='utf8')
# for line in f:
#     print(f'line = {line}',end='')
# f.close()
# # end参数就表示每次打印之后要在末尾加个啥(默认是\n)，修改成空字符串''就是啥都不加

# 3、还可以使用 readlines 方法直接把整个文件的所有内容都读出来，按照行组织到一个列表里
# f = open('D:/Python_code/python_code/Python基础语法第六篇/test.txt','r',encoding='utf8')
# lines = f.readlines()
# print(lines)
# f.close()
# 每一行的末尾都有\n：['床前明月光\n', '疑是地上霜\n', '举头望明月\n', '低头思故乡']
# 和前面的 for 循环相比，好处就是它一次就读完了（硬盘操作，读的次数越多，耗时越长，分多次读不如一次读完）
# 内存很大的东西一次读完，前提是内存足够大