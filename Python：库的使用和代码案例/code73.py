# 代码案例：操作excel

# 操作 excel
import  xlrd

# 1、先打开 xlsx 文件
xlsx = xlrd.open_workbook('C:/Users/18106/Desktop/比特课程学习课件/Python/Python：Excel操作.xlsx')
# 2、获取到指定的标签页
table = xlsx.sheet_by_index(0)
# 3、获取到表格中有多少行
nrows = table.nrows
# 4、进行循环统计操作
total = 0
count = 0
for i in range(1,nrows):
    # 拿到当前同学的班级
    classID = table.cell_value(i,1)
    if classID == 100:
        total += table.cell_value(i,2)
        count += 1
print(f'平均分: {total / count}')