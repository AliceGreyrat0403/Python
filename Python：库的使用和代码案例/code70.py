# 文件搜索工具

# 很多目录，很多文件，想找到某个文件，就不太容易
# 文件搜索工具——如everything

# 实现文件查找工具
# 输入要查找的路径，输入要搜索的文件名（一部分）
# 自动地在指定的路径进行查找
# import os
#
# inputPath = input('请输入要搜索的路径:')
# pattern = input('请输入要搜索的关键词:')

# 递归查找，遇到子目录，就进到目录里面进行查找
#OS.walk（OS：操作系统），只需要使用简单的循环就可以完成递归遍历的过程，就不必手写递归代码了
# for dirpath,dirnames,filenames in os.walk(inputPath):
#     print('----------------------------')
#     print(f'dirpath = {dirpath}')
#     print('dirnames:')
#     for name in dirnames:
#         print(name)
#     print('filename:')
#     for name in filenames:
#         print(name)

# dirpath: 遍历到当前位置，对应的路径是啥
# dirnames: 当前目录下，都有哪些目录，是一个列表，可以包含多个目录名
# filenames: 当前目录下，都有哪些文件名，是一个列表，可以包含多个文件名
# os.walk: os.walk 每次调用都能自动的去针对子目录进行递归的操作，只需要使用上述循环就可以把所有的路径都获取出来

# 正式实现一下这里的功能
import os

inputPath = input('请输入要搜索的路径:')
pattern = input('请输入要搜索的关键词:')

for dirpath,_,filenames in os.walk(inputPath):
    for f in filenames:
        if pattern in f:
            print(f'{dirpath}/{f}')
# 这里只是一个简单粗暴的遍历，比不了 everything，不算特别高效