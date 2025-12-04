# 函数的链式调用和嵌套调用(2)

# 嵌套调用

# def test():
#     print("Alice")
#
# test()

# 嵌套调用层次可以有很多层

# def a():
#     print('函数 a')
#
# def b():
#     print('函数 b')
#     a()
#
# def c():
#     print('函数 c')
#     b()
#
# def d():
#     print('函数 d')
#     c()
#
# d()
# # 运行结果
# 函数 d
# 函数 c
# 函数 b
# 函数 a

# 代码顺序稍作调整，打印顺序就会变化

def a():
    print('函数 a')

def b():
    a()
    print('函数 b')

def c():
    b()
    print('函数 c')

def d():
    c()
    print('函数 d')

d()
# # 运行结果
# 函数 a
# 函数 b
# 函数 c
# 函数 d