# 空语句pass

# 输入一个数字, 如果数字为 1, 则打印 hello

# 单一个if语句
# a = input("请输入一个数字：")
# if a == '1':
#     print("hello")

# 歪脑筋
a = input("请输入一个数字：")
if a == '1':
    # 啥都不做
    # 虽然希望条件满足的时候，啥都不做，但是由于Python对于语法格式尤其是缩进和代码块要求较高，
    # 所以如果啥都不写（只写个注释）是不符合语法要求的
    # 这种情况下，可以使用空语句进行占位
    pass
    # 在写条件或者循环的时候
    # 很多地方都是如此，虽然我们啥都不想做，但是也得写个pass空语句来占位！防止空着导致代码编译出错
else:
    print("hello")
# 报错：IndentationError: expected an indented block after 'if' statement on line 12
# expected an indented block after 'if'：预期应该有一个带有缩进的代码块在if后面
