# 字典的遍历

# 直接使用 for 循环来遍历字典
# a = {
#     'id' : 1,
#     'name' : 'zhangsan',
#     'score': 90
# }
#
# for key in a:   # 把每个键取出来，并且获取到每个键值对的键和值
#     print(key,a[key])

# 取出所有 key 和 value
# a = {
#     'id' : 1,
#     'name' : 'zhangsan',
#     'score': 90
# }
# print(a.keys())
# print(a.values())
# print(a.items())

# 借助上面的方法也一样能完成对字典的遍历
a = {
    'id' : 1,
    'name' : 'zhangsan',
    'score': 90
}

for key,value in a.items():
    print(key,value)