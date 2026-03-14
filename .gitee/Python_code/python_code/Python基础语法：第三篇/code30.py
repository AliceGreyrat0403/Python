# 函数的定义和调用

# 返回值 = 函数名（实参列表）

# 先定义一个函数
# 如果只是定义，而不去调用，则函数体里面的代码就不会执行！
def test():
    print('Alice')
    print('Alice')
    print('Alice')

# 函数调用才会真正执行函数体里面的代码
# 函数经过一次定义之后，可以被调用多次！
test()
test()
test()
test()
test()

# 运行结果：
# Alice
# Alice
# Alice
# Alice
# Alice
# Alice
# Alice
# Alice
# Alice
# Alice
# Alice
# Alice
# Alice
# Alice
# Alice

# Python中要求，函数定义写在前面，函数调用写在后面-->先定义，后调用