arr = [4, 2, 3, 1, 5]


# 暴力法：维护一个最大长度，检测到下一个数字比本数字大，
# 就将当前下标改为该数字对应下标继续和下一个数字比较，增加计数
# 最大长度记录以后开始第二层迭代
def violence():
    maxCnt = 0
    for i in range(len(arr)):
        p = i
        cnt = 1
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[p]:
                cnt += 1
                p = j
        maxCnt = max(maxCnt, cnt)
    return maxCnt


def dp():
    dpArr = [0]*(len(arr))
    for i in range(len(arr)):
        cnt = 1
        for j in range(i-1, -1, -1):
            if arr[i]>arr[j]:
               cnt = max(cnt,dpArr[j]+1)
        dpArr[i] = cnt
    ret = max(dpArr)
    return ret

r = dp()
print(r)
