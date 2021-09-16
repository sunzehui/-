# 题目：输入一个正整数数组，把数组里所有整数拼接起来排成一个数，
# 打印出能拼接出的所有数字中最小的一个
# 输入：3 32 321
# 输出：321323

def sort(arr):
    res = ""
    arr = list(map(str, arr))
    # 转成字符串,两两一组合,哪个组合小就添加到最终的数据里
    for i in range(0, len(arr) - 1):
        s1 = arr[i]+arr[i+1]
        s2 = arr[i+1]+arr[i]
        m = min(s1,s2)
        res += m
    return int(res)


arr = [3, 32, 321]
res = sort(arr)
print(res)
