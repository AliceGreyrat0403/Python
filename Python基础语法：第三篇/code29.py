# 使用函数的方式来解决刚才的问题：
# 有什么地方要改也只要改一次就好了

# 定义一个求和函数
def calcSum(beg,end):
    theSum = 0
    for i in range(beg,end + 1):
        theSum += i
    print(theSum)   # 跟for同一级缩进

# 调用函数
# 求1 - 100的和
calcSum(1,100)
#求300 - 400的和
calcSum(300,400)
# 求1 - 1000的和
calcSum(1,1000)