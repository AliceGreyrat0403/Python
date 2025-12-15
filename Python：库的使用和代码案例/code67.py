# 代码案例：日期计算器（日期之间作差）

# datetime
# import datetime # (import)导入对应的模块
# # 先构造 datetime 变量
#
# # datetime.datetime（模块名.类型名）
# date1 = datetime.datetime(2006,12,14)
# date2 = datetime.datetime(2025,12,14)
# # 也可以通过关键字参数传
# # date1 = datetime.datetime(year=2025,month=12,day=14)    # 更加直观
# print(date2 - date1)    # 两种相减可得出相差多久

# # 这样写还有点别扭，我们可以直接这样写
# from datetime import datetime   # 变成从datetime模块import一个datetime类型
# # 通过这样的改变，让我们后续无需再写[datetime.] --> [模块名.]的方式——改进的写法
#
# # 先构造 datetime 变量
# date1 = datetime(2006,12,14)
# date2 = datetime(2025,12,14)
# print(date2 - date1)    # 结果完全一样

# 还有一种写法：既能在这行代码中知道模块名是什么，也能体现出后续构造的对象是什么类型
# 比较直观
import datetime as dt   # 还是datetime模块导入，但是给datetime取了一个别名dt，通过dt代表了datetime
# 通过这样的改变，让我们后续无需再写[datetime.] --> [模块名.]的方式——改进的写法

# 先构造 datetime 变量
date1 = dt.datetime(2006,12,14)
date2 = dt.datetime(2025,12,14)
print(date2 - date1)    # 结果完全一样

# 判断星期几、格式化硬件打印时间戳……