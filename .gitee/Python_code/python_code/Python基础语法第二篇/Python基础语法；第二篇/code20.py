# 条件语句练习（1）

# (1) 输入一个整数, 判定是否是奇数
# a = input("请输入一个整数：")   # 报错：TypeError: not all arguments converted during string formatting
# a = int(input("请输入一个整数："))  # 问题解决
#
# if a % 2 == 0:
#     print("偶数")  # 除尽
# else:
#     print("奇数")  # 除不尽

# 反过来可不可以呢？这个代码在C++/Java中是不太行的
# if a % 2 == 1:
#     print("奇数")  # 除尽
# else:
#     print("偶数")  # 除不尽

# 那余一个负数呢？
# 输出：奇数
# -19 % 2 =>-1，和1是不相等的
# 在 Python 中
# -19 % 2 =>1
# 因此这个代码是ok的！

# 用户输入啥都有可能，如果输入一个字符串呢？
# 报了一个异常-->ValueError: invalid literal for int() with base 10: 'abc'
# with base 10:按照十进制来解析的
# int()转换默认是按照十进制的方式来解析的

# 条件语句练习（2）

# (2) 输入一个整数, 判定是正数还是负数
# a = int(input("请输入一个整数："))
# if a > 0:
#     print("正数")
# elif a < 0:
#     print("负数")
# else:
#     print("0")

# (3) 判定年份是否是闰年
# 每隔4年一次闰年
# 如果年份能够被100整除，（1000,1900,2000），这是世纪闰年，得看能否被 400 整除！
year = int(input("请输入一个年份："))
# if year % 100 == 0:
#     # 世纪闰年的判定
#     if year % 400 == 0:
#         print("闰年")
#     else:
#         print("平年")
# else:
#     # 普通闰年的判定
#     if year % 4 == 0:
#         print("闰年")
#     else:
#         print("平年")

# or的左边针对普通年份，or的右边针对世纪年份
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("闰年")
else:
    print("平年")

# 上面关于闰年的代码，还是第一种方法更好
# 还是不要用代码的行数来衡量可读性
# 第一种方法这一段代码，目的性更明显，平铺直叙
# 第二种方法这一段代码虽然代码变短了，但是中间夹杂了一些更复杂的条件判定，可读性不如第一种方法