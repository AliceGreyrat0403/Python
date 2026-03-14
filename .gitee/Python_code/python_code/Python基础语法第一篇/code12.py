# 逻辑运算符

# 找女朋友，谈婚论嫁——要彩礼
# 要有房并且要有车（and：缺一不可）
# 要有房或者要有车（or：有一个就行，不能两个都没有

# and 并且    两侧操作数均为True，表达式的值为True，否则为 false（一假则假）
# or  或者    两侧操作数均为False,表达式的值为False，否则为 True（一真则真）
# not 逻辑取反 只有一个操作数.操作数为True，则返回False；操作数为False，则返回True

a = 10
b = 20
c = 30

# # 1. and
# # a < b < c等价于 a < b and b < c
# # print(a < b and b < c)
# print(a < b < c) # 带黄色波浪线，功能上没问题，但是有更好的写法：点击黄色灯泡
# print(a > b and b > c)
#
# # 2. or
# print(a < b or b < c)
# print(a < b or b > c)
# print(a < b or b < c)
#
# # 3. not
# print(not a < b)
# print(not a > b)

# 比如C++或者Java里，使用
# &&表示逻辑与   并目
# ||表示逻辑或   或者
# ！表示逻辑非   逻辑取反

# 逻辑运算符中的重要细节：短路求值（物理上的术语）
# 对于and操作来说：如果左侧表达式为False，那么整体的值一定是False，右侧表达式不必求值！
# 对于or操作来说：如果左侧表达式为True，那么整体的值一定是True，右侧表达式不必求值！

# 右侧就不再求值了，所以一旦右侧求值了，是能够看到代码出现异常的！
# 如果代码没有抛出异常，右侧没有求值！
print(a > b and 10 / 0 == 1)
# print(a < b and 10 / 0 == 1)    # 报错：ZeroDivisionError: division by zero
print(a < b or 10 / 0 == 1)

# 短路求值这种行为，大部分编程语言都有，C、C++、Java……