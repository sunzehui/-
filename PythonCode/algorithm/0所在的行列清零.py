# 如果矩阵中某个元素为0，则将其所在的行和列清零
# 1   2  3  4
# 5   6  0  8
# 9   0  11 12
# 13  14 15 16
# 输出：
# 1   0  0  4
# 0   0  0  0
# 0   0  0  0
# 13  0  0 16
arr = [
    [1, 2, 3, 4],
    [5, 6, 0, 8],
    [9, 0, 11, 12],
    [13, 14, 15, 16]
]


def printArr(arr):
    colArr = [0]*len(arr)
    rowArr = [0]*len(arr[0])
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 0:
                rowArr[i] = 1
                colArr[j] = 1
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if colArr[j] == 1 or rowArr[i] ==1:
                arr[i][j] = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            print(arr[i][j],end=" ")
        print()

printArr(arr)
