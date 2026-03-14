# 实现一个命令行版本的学生管理系统
import sys

# 使用这个全局变量，来管理所有的学生信息
# 这个列表的每个元素都是一个“字典”，每个字典就分别表示了一个同学！
students = []   # 数据保存在这样一个变量里面，变量容易丢失数据，为了持续保存，需要存在一个文件里面

def menu():
    print('1. 新增学生')
    print('2. 显示学生')
    print('3. 查找学生')
    print('4. 删除学生')
    print('0. 退出程序')
    choice = input('请输入您的选择: ')
    # return int(choice)  # 转成选项
    # 或者直接以字符串的形式
    return choice

# 实现增删查功能

def insert():
    print('【新增学生】开始！')
    studentID = input('请输入学生的学号:')
    name = input('请输入学生的姓名:')
    gender = input('请输入学生的性别:')
    if gender not in('男，女'):
        print('性别输入的内容不符合要求，新增失败!')
        return
    className = input('请输入学生的班级:')
    # 使用一个字典把上述的信息给聚合起来
    student = {
        'studentId':studentID,
        'name':name,
        'gender':gender,
        'className':className
    }
    global students
    students.append(student)    # 通过 append 新增学生

    print('【新增学生】完毕！')

def show():
    # 遍历全局变量的这个列表，把每个学生的信息打印出来
    print('【显示学生】开始！')
    for s in students:
        print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")  # 通过制表符分隔开
    print(f'【显示学生】完毕！共显示了{len(students)}条数据!')

def find():
    # 改进学生姓名，来进行查找
    print('【查找学生】开始!')
    name = input('请输入要查找的同学姓名: ')
    count = 0
    for s in students:  # students(全局变量)，读取全局变量的时候不需要加 global 去修饰，修改时才需要加
        if name == s['name']:
            print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")
            count += 1
    print(f'【查找学生】结束!共找到了{count}个匹配的同学!')

def delete():
    print('【删除学生】开始！')
    studentId = input('请输入要删除的学生学号:')
    # 看看这个学号对应的同学是哪个字典，然后把这个字典从列表里面删掉就好了
    for s in students:
        if studentId == s['studentId']:
            print(f"删除{s['name']}同学的信息!")
            students.remove(s)
    print('【删除学生】完毕！')

def main():
    """
    入口函数
    """
    # 通过控制台和用户进行交互
    print('-----------------------------------------------')
    print('               欢迎来到学生管理系统                ')
    print('-----------------------------------------------')
    while True:
        # 通过 menu 函数来打印出菜单项
        choice = menu()
        if choice == '1':
            # 新增学生
            insert()
        elif choice == '2':
            # 显示所有学生
            show()
        elif choice == '3':
            # 查找学生
            find()
        elif choice == '4':
            # 删除学生
            delete()
        elif choice == '0':
            # 退出程序
            print('goodbye!')
            sys.exit(0)
        else:
            print('您的输入有误！请重新输入！')
            # 需要进入下次循环，让用户重新输入
            # continue

# 存储在内存里面的数据是容易丢失的！

main()