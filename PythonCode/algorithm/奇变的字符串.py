inp = "abcdefg"
# 将输入的字符串转为数组
arr = list(inp)
# 从0开始取出所有奇数索引元素
ret = arr[1::2]
ret.reverse()

for i in range(0, len(ret)):
    # 将奇数位替换
    arr[i*2+1] = ret[i]

print("".join(arr))
