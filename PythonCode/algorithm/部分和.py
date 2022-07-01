# 输入：
# n = 4
# a = {1,2,4,7}
# k=13
# 输出：
# Yes{13 = 2+4+7}
def solution(n, arr):
    newArr = []
    if n == 0:
        newArr.append([arr[0]])
        newArr.append([])
        return newArr
    oldArr = solution(n - 1, arr)
    # print(oldArr)
    for i in oldArr:
        newArr.append(i)
        clone = i.copy()
        clone.append(arr[n])
        newArr.append(clone)
    return newArr


arr = solution(3, [1, 2, 4, 7])
for i in arr:
    res = 0
    for j in i:
        res += j
    if res == 13:
        print(i)

