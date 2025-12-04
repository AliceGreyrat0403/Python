# 函数的链式调用和嵌套调用(1)

# 链式调用
def isOdd(num):
    if num % 2 == 0:
        return False
    return True

def add(x,y):
    return x + y

# result = isOdd(10)
# print(result)

print(isOdd(add(5,5)))