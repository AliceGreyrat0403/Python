# break和continue
# continue立即结束当前这次循环，进入下次循环
# break立即结束整个循环

# 假设我要吃 5 个包子
for i in range(1,6):
    if i == 3:
        # 发现第三个包子，有一只虫
        continue
    print(f'吃第{i}个包子')

# 还是要吃 5 个包子
for i in range(1,6):
    if i == 3:
        # 发现第三个包子，有半只虫
        break
    print(f'吃第{i}个包子')


# 给定若干个数字，求平均值（也不知道几个数字）
# 这个变量表示加和的结果
theSum = 0
# 这个变量表示有几个数字
count = 0
while True:     # 会不会变成死循环？光看到while True 不一定是死循环，关键是看循环体里是不是还能break
    # 没啥营养，但却要反复执行的
    num = input("请输入一个数字(分号表示输入结束)：")
    if num == ";":
        # 约定当用户输入 ; 的时候，表示输入结束
        break
    num = float(num)
    theSum += num
    count += 1

print(f'平均值为：{theSum / count}')