# 代码示例：字符串操作

# 代码案例：单词逆序（剑指offer中的题目）
# 剑指offer:是一本包含很多算法题的书！
# 每个参加秋招的同学都至少把这本书刷个两遍！很多面试官出算法题就是从这本书里找的！
# 如果真的遇到了原题，千万不要表现出来！这时候就到了考验演技的时候了！
# 可以多“思考”一下，读读题，不要一口气写完，停顿一下

# 题目：怎样区分的单词？根据空格来分割
# 在Python中，思路是这样的：
# 1、针对上述字符串，使用空格进行划分
# 字符串 split 方法，可以指定分隔符，把字符串分成多个部分，放到一个 list 里
# 2、针对刚才的切分结果列表，进行逆序(reverse方法)
# 3、再把逆序后的列表，组合起来(join，并且可以在组合指定分隔符为1个空格)

def reverseWords(s:str):    # s:[类型声明]，这样下面就有提示了（变量有了类型声明之后）
    tokens = s.split(' ')  # 没有代码提示：是因为Python是动态类型的语言，所以我们写s的时候，
    # 其实Pycharm是不知道s是什么类型的，不知道是啥类型，也就不知道有哪些方法，
    # 所以s.spilt到底能不能调用，以及有没有其它方法，这是不好确定的
    tokens.reverse()    # 逆序
    return ' '.join(tokens) # 借助空格分隔符，把这里的字符串重新拼接成一个更长的字符串

# 输入一个字符串，运行程序
print(reverseWords("I am a student."))

# 代码案例：旋转字符串
# 题目要求
# 如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true
# s = "abcde"   "bcdea"     "cdead"     "deabc"     "eabcd"(s通过旋转能得到的内容)
# 把最左侧的字符，给放到最右侧去！
# s + s => "abcdeabcde" # 每个旋转后得到的字符串都可以在这样一个大字符串中找到

def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)  # in判断某个字符串是否是另外一个字符串的子串

print(rotateString("abcde","cdeab"))
print(rotateString("abcde","edcba"))