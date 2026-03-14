# 循环语句-->反复执行
# Python一共有两种循环：while循环和for循环
import math

# while循环（1）
# Python中“:”很常用，很多时候是作为[条件结束]的这样一个概念
# 因为Python中没有“()”，从哪到哪是一个条件需要一个区分——“:”

# 打印1 ~ 10的整数

# 这是一个最简单的while循环语句
# 实际上暗藏玄机-->包含了循环最基本的条件
# 1. 循环变量的初始值
# 2. 循环的判定条件
# 3. 循环变量的更新语句
# num = 1
# while num <= 10:
#     print(num)
#     num = num + 1

# 如果把最后的num = num + 1注释掉会怎么样？-->会死循环1，要点击红色正方形终止，并且编译器会报一个警告
# 死循环报错：
# Traceback (most recent call last):
#   File "D:\Python_code\python_code\code23.py", line 24, in <module>
#     print(num)
# KeyboardInterrupt
# 由于忘记写了更新循环变量的语句
# 循环会一直执行，停不下来了，直到手动强制结束程序
# 形如这样的代码就叫做“死循环”代码
# num = 1
# while num <= 10:
#     print(num)
#     # num = num + 1
# 死循环很多时候是bug。也有些时候不是bug
# 像我们现在学习的时候写的死循环是bug，但是像服务器（7 * 24小时运行）一直等着客户端连过来
# -->因此服务器的代码中经常需要一些死循环，保证程序是在不断运行、不断工作的

# while循环（2）
# 计算1 ~ 100的和
# sum变量用于表示计算的和
# sum = 0
# num = 1
# while num <= 100:
#     sum = sum + num
#     num += 1
#
# print(f'sum = {sum}')
# # 运行结果：5050

# 计算5的阶乘
# result = 1
# num = 1
# while num <= 5:
#     result *= num
#     num += 1
# print(f'result = {result}')

# 求和1! + 2! + 3! + 4! + 5!
num = 1
# sum表示最终的加和结果
sum = 0
# 两层循环，外层循环来控制加和
while num <= 5:
    # 先计算出当前num!是多少，往sum上进行累加
    # factorResult表示n!的值
    factorResult = 1
    i = 1
    # 内存循环来控制求阶乘
    while i <= num:
        factorResult *= i
        i += 1
    sum += factorResult
    num += 1

print(f'sum = {sum}')