# 字典查找key

# 1、使用 in 来判定某个 key 是否在字典中存在
# a = {
#     'id' : 1,
#     'name' : 'zhangsan'
# }
#
# print('id' in a)
# print('classId' in a)
#
# # in 只是判定 key 是否存在，和 value 无关！
# print('zhangsan' in a)
#
# # not in 用来判定 key 在字典中不存在
# print('id' not in a)
# print('classId' not in a)

# 2、使用 [] 来根据 key 获取到 value
# in、not in只能判定在不在，而 [] 可以获取里面的内容
a = {
    'id' : 1,
    'name' : 'zhangsan',
    100 : 'lisi'
}

print(a['id'])  # 光是一个 id 只是代表一个 key，但是 a['id'] 这个是根据 key 找到对应的 value，这里就是1
print(a['name'])    # 这样 zhangsan 也能获取到了
print(a[100])   # 整数也可以
print(a['classId']) # 代码出现异常：KeyError: 'classId'（表示当前这个key在字典中不存在）
# (1)对于字典来说，使用in或者[]来获取value(字典背后使用了特殊的数据结构：哈希表——特点：擅长查找操作)，都是非常高效的操作
# (2)对于列表来说，使用in比较低效的(需要把整个列表遍历一遍)，而使用[](类似于数组 / 顺序表取下标)是比较高效的
# 像哈希表、顺序表这样的数据结构都是日常开发中比较常用的结构，Python把这些数据结构封装好了，作为一个内置类型
# 我们拿过来就可以很方便地使用，只不过我们使用时要注意理解这些结构背后操作的一些相关机制，
# 以及这些操作带来的一些效率高低的问题