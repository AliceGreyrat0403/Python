# 代码案例：统计字符串前缀
# 遍历 words，取出每个字符串，判定当前这个字符串是否是 s 的前缀即可(s是否是以这个字符串开题的)

def countPrefixes(words: list,s: str):
    count = 0
    for word in words:
        if s.startswith(word):  # 使用 in 操作可以判断 word 是不是 s 的一部分
            # s 是以 word 开头
            count += 1
    return count    # 注意缩进

print(countPrefixes(['a','b','c','ab','bc','abc'],'abc'))
print(countPrefixes(['a','a'],'aa'))