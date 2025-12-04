# 函数的参数(2)
# 形参和实参

# def test(a):
#     print(a)
#
# test(10)
# test('hello')
# test(True)

def add(a,b):
    return a + b

print(add(10,20))   # 整型相加
print(add(1.5,2.5)) # 浮点型相加
print(add('hello','world')) # 字符串相加
print(add(10,'hello'))  # 报错，不能相加