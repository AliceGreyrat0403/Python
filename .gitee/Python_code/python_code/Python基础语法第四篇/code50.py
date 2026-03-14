# 列表的查找和删除
# 一、查找元素

# 1、使用 in 来判定某个元素是否在列表中存在
# a = [1,2,3,4]
# print(1 in a)   # 用 in 这样一个运算符就搞定了！
# print(10 in a)  # 存在返回True，不存在返回False
# print(1 not in a)
# print(10 not in a)

# 2、使用 index 方法来判定当前元素在列表当中的位置，得到了一个下标
# a = [1,2,3,4]
# print(a.index(2))   # 2的下标
# print(a.index(3))   # 3的下标
# print(a.index(10))  # 10的下标这里不存在，Python语言允许下标为负数，其他语言下标不能为负数，返回的是-1
# # 运行结果：抛出异常 ---> ValueError: 10 is not in list（10并不在列表当中）