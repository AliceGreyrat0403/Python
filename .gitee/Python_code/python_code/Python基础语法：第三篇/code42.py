# 函数形参的默认值

# 通过这样的默认值，就可以让函数的设计更灵活！
# debug：形参的默认值
# 带有默认值的形参就可以在调用函数的时候，不必传参
# 参数越多会提高使用者的成本
def add(x ,y ,debug=False):
    if debug:
        print(f'x = {x},y = {y}')
    return x + y

# result = add(10,20) # 不开启调试信息的情况，只传了两个实参
result = add(10,20,True)
# result = add(10,20,False)
print(result)
# 像默认值这样的语法，在编程界是存在争议的！
# C++也支持形参默认参数，Java就不支持，但是Python还是引入默认参数的

# 带有默认值的形参得在形参列表的后面，而不能在前面 / 中间！
# 多个带有默认值的形参，这些都得在形参列表的后面
# 报错：SyntaxError: parameter without a default follows parameter with a default