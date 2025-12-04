# 函数递归

# 写一个函数，来求 n 的阶乘(n 是正整数)

# 用循环的方式来写
# def factor(n):
#     result = 1
#     for i in range(1,n + 1):
#         result *= i
#     return result
#
# print(factor(5))

# 用递归的方式来写
# n! => n * (n - 1)
# 1! => 1
def factor(n):
    if n == 1:
        return  1
    return n * factor(n - 1)

print(factor(5))