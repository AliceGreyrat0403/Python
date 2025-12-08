# 字典的创建
# 我们此处所说的Python中的字典表示一种存储键值对的数据结构

# # 1、创建字典
# a = {}
# print(type(a))
# b = dict()
# print(type(b))
#
# # 2、创建字典的同时设置初始值
# a = {'id' : 1,'name' : 'zhangsan'}
# print(a)

# 上面的写法都不够直观
a ={
    'id' : 1,
    'name' : 'zhangsan'
}
print(a)
# 打印出来还是这种比较紧凑的格式：{'id': 1, 'name': 'zhangsan'}
# 但是书写代码的时候可以写成这种多行的形式——好处就是一目了然，可读性很好

b ={
    'id' : 1,
    'name' : 'lisi',    # 最后一个键值对后面的逗号可以写也可以不写！
}
print(b)