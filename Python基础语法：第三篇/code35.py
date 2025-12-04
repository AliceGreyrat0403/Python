# 函数的返回值（2）

# 这种情况下，不算是有多个 return 语句
# def test1():
#     return 1
#     return 2

# 一般多个 return 语句是搭配分支/循环语句的

# def isOdd(num):
#     """
#     用来判定 num 是不是奇数，如果是奇数就返回 True，不是就返回 False
#     :param num:要判定的整数
#     :return:返回 True False 表示是不是奇数
#     """
#     # 第一种写法
#     # if num % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#
#     # 第二种写法
#     if num % 2 == 0:
#         return False
#     return True
#
# print(isOdd(10))
# print(isOdd(19))

# 写一个函数，返回平面上的一个点
# 横坐标，纵坐标
def getPoint():
    x = 10
    y = 20
    return x,y

a,b = getPoint()
print(a,b)