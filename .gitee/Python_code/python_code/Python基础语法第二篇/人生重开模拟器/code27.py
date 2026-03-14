# 人生重开模拟器
import random   # 神不知鬼不觉出现个import语句-->把这个删掉，下面的random语句也删掉再重写，就能再次生成import语句
import sys
import time

# 对于Pycharm来说，有一个功能：能够自动导入当前使用的模块

# 欢迎界面
print('+----------------------------------------------------+')
print('|                                                    |')
print('|                花有重开日，人无再少年                  |')
print('|                                                    |')
print('|                欢迎来到人生重开模拟器                  |')
print('|                                                    |')
print('+----------------------------------------------------+')

# 设置初始属性（逻辑实现）
# 分成四个部分属性：颜值，体质，智力，家境，总和不能超过20，初始情况下每一项取值都是1 ~ 10之间
while True:     # 玩家可能是手滑了，多给几次机会；while True不一定是死循环
    print("请设置初始属性(可用总点数为：20)")
    face = int(input("请输入颜值(1 - 10)："))
    strong = int(input("请输入体质(1 - 10)："))
    iq = int(input("请输入智力(1 - 10)："))
    home = int(input("请输入家境(1 - 10)："))

    # 通过条件语句对用户输入的属性进行校验检查
    # 这段逻辑，使用 elif 是否可以呢？完全可以，效果是相同的
    # 使用 elif 则是多个分支只能进一个，一旦某个条件满足了，就不会再走其它的分支了
    # 此处虽然没有使用 elif ，但是有了 continue ，一旦某个条件满足， continue 就会使循环从头再来，
    # 也就没机会执行后续的条件判定了。
    if face < 1 or face > 10:
        print("颜值设置有误!")
        # 输入有误怎么办？好的措施是让玩家再输入一次
        continue    # 立即结束此次循环，进入下一次循环
    if strong < 1 or strong > 10:
        print("体质设置有误!")
        continue    # 立即结束此次循环，进入下一次循环
    if iq < 1 or iq > 10:
        print("智力设置有误!")
        continue    # 立即结束此次循环，进入下一次循环
    if home < 1 or home > 10:
        print("家境设置有误!")
        continue    # 立即结束此次循环，进入下一次循环
    # 判断一下四个属性相加有没有超过20
    if face + strong + iq + home > 20:
        print("总的属性和超出了20，也是设置有误!")
        continue

    # 如果当前上面的条件都没有被触发，则认为玩家的属性数据是合法的
    # 此时就可以跳出循环结束输入了
    print("初始属性输入完毕!")
    print(f"颜值：{face}，体质：{strong}，智力：{iq}，家境：{home}")
    break   # 跳出while True循环

    # 生成一下角色性别
    # random.randint(beg,end)，就能生成[beg,end]之间的随机整数-->前闭后闭区间
    # random.randint-->此处的random是一个Python中的模块（比如==别人写好的代码，我们直接来用）！
    # 咱们非要使用别人写好的模块嘛？也不一定，很多功能咱们自己也不是不能实现，但是使用别人写好的。会比较筒单方便
    # 使用别人模块的优点：
    # 1.降低编程的门槛~有的东西咱们自己不会写也没事，可以直接用别人的
    # 2.使用别人的模块，就可以更快速的完成需要实现的功能
point = random.randint(1,6)     # 生成一个随机数
# print(f'point = {point}')
if point % 2 == 1:
    gender = 'boy'
    print("你是个男孩")
else:
    gender = 'girl'
    print("你是个女孩")

# 设置角色的出生点
# 为了简单一点，就直接生成 1~3 的随机数
point = random.randint(1,3)     # 类似投骰子
if home == 10:
    # 第一档
    print('你出生在帝都，你的父母是贵族')
    home += 1
    iq += 1
    face += 1
elif 7 <= home <= 9:
    # 第二档
    if point == 1:
        print("你出生在大城市，你的父母是高官政要")
        face += 2
    elif point == 2:
        print('你出生在大城市，你的父母是富商')
        home += 2
    else:
        print('你出生在大城市，你的父母是大学教授')
        iq += 2
elif 4 <= home <= 7:
    if point == 1:
        print('你出生在三四线城市，你的父母是公务员')
        face += 1
    elif point == 2:
        print('你出生在三四线城市，你的父母是教师')
        iq += 1
    else:
        print('你出生在三四线城市，你的父母是医生')
        strong += 1
elif 2 <= home <= 3:
    if point == 1:
        print('你出生在六七线小城市，你的父母是工人')
        strong += 1
    elif point == 2:
        print('你出生在小镇上，你的父母是服务员')
        face += 1
    else:
        print('你出生在小镇上，你的父母是个体户')
        iq += 1
else:
    if point == 1:
        print('你出生在农村，你的父母是辛苦劳作的农民')
        face -= 1
    elif point == 2:
        print('你出生在穷乡僻壤，你的父母是无业游民')
        home -= 1
    else:
        print('你出生在镇上，你的父母感情不和')
        strong -= 1
print(f'颜值：{face}，家境：{home}, 智力：{iq}, 体质： {strong}')

# 人生不同阶段的人生经历
# 幼年阶段
for age in range(1, 11):
    # 把一整年的打印都整理到一个字符串中，在这一年的结尾统一打印
    info = f'你今年{age}岁。'
    # 生成一个[1,3]的随机整数
    point = random.randint(1, 3)
    # 接下来编写各种事件的代码
    # 性别触发的事件
    if gender == 'girl' and home <= 3 and point == 1:
        info += '你的家里人重男轻女思想很严重，你被遗弃了！'
        print(info)
        point('游戏结束！')
        sys.exit(0)
    # 体质触发的事件
    # 使用 elif 是为了保证每年只触发一个事件！
    elif strong <= 5 and point < 3:
        info += '你生了一场大病'
        if home >= 5:
            info += '在父母的悉心照料之下，你不久便康复了'
            strong += 1
            home -= 1
        else:
            info += '你父母没有精力管你，你的身体状况更糟糕了'
            strong -= 1
    # 颜值触发的事件
    elif face <= 4 and age > 7:
        info += '你长得太磕碜了，其他小朋友都不乐意跟你玩'
        if iq >= 5:
            info += '你决定用学习来充实自己！'
        else:
            if gender == 'boy':
                info += '你和别的小朋友经常打架！'
                strong += 1
                iq -= 1
            else:
                info += '你经常被别的小朋友欺负！'
                strong -= 1
    # 智力触发的事件
    elif iq <= 5:
        info += '你看起来傻乎乎的。'
        if home >= 8 and age >= 6:
            info += '你的父母把你送到更好的学校去学习'
            iq += 1
        elif 4 <= home <= 7:
            if gender == 'boy':
                info += '你的父母鼓励你多运动，争取成为运动员'
                strong += 1
            else:
                info += '你的父母鼓励你多打扮打扮自己'
                face += 1
        else:
            # 家境 < 4
            info += '你的父母为此经常吵架'
            if point == 1:
                strong -= 1
            elif point == 2:
                iq -= 1
            else:
                pass
    # 健康成长事件
    else:
        info += '你健康成长了！'
        if point == 1:
            info += '你的身体看起来更加结实了'
            strong += 1
        elif point == 2:
            info += '你看起来更加漂亮了'
            face += 1
        else:
            # 无事发生
            pass

    # 打印这一年发生的事情
    print(info)
    print(f'颜值：{face}，体质：{strong}，智力：{iq}，家境：{home}')
    print('-------------------------------------------------')
    # 为了方便观察，加一个小小的暂停操作
    time.sleep(1)