# 函数的返回值（1）

# 求beg，end这个范围的整数之和
def calSum(beg, end):
    theSum = 0
    for i in range(beg,end + 1):
        theSum += i
    return theSum

result = calSum(1,100)
print(result)