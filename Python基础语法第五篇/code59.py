# 可哈希的类型
# 使用 hash 函数能够计算出一个变量的哈希值
# hash 是一个内建函数，可以直接使用
print(hash(0))   # 0 的哈希值就是 0
print(hash(3.14))   # 浮点数
print(hash('hello')) # 字符串
print(hash(True)) # 布尔类型
print(hash((1,2,3))) # 元组

# 上面这些类型都是能够计算出哈希值的（都能作为字典的 key ）
# 有的类型是不能计算出哈希值的 ——> 列表、字典都是不可哈希的（不都能作为字典的 key ）
# print(hash([1,2,3,4]))  # list这样的类型会报错：TypeError: unhashable type: 'list'
# print(hash({})) # 字典类型不能计算哈希值：TypeError: unhashable type: 'dict'

# 什么样的类型是可哈希的？
# （1）不可变的对象，一般就是可哈希的
# （2）可变的对象，一般就是不可哈希的

# 小结
# 字典，列表，元组 ——> Python中非常常用的内置类型，相比于int，str，float...
# 它们内部可以再包含其他元素了
# 容器 / 集合类
# 字典，列表，元组——>Python内部提供的容器