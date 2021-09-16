def arraySumBiggest(arr):
    sumNum = arr[0]
    # 维护一个最大值
    maxNum = sumNum
    for i in range(1, len(arr)):
        # 累加和比0大的时候继续累加
        if sumNum >= 0:
            sumNum += arr[i]
        else:
            # 累加和小于0，丢弃，从当前重新开始计算
            sumNum = arr[i]
        # 当前累加和大于最大值时更新最大值
        if sumNum > maxNum:
            maxNum = sumNum

    return maxNum

def dpArrayMaxSum(arr):
    dp = arr.copy()
    for i in range(1,len(dp)):
        dp[i] = max(dp[i-1]+arr[i],arr[i])
    return max(dp)


def solution(matirx):
    M = len(matirx)
    N = len(matirx[0])
    # 历史最大值
    maxNum = 0
    # 从第0行开始,以每行作为起点,将列最大值计算出来
    startRow = 0
    while startRow < M:
        colSum = [0] * N
        for i in range(startRow, M):
            # 每一列的和

            for j in range(0, N):
                colSum[j] += matirx[i][j]
            # 计算每个起始行的最大值序列
            _max = arraySumBiggest(colSum)

            # 更新最大值
            if _max > maxNum:
                maxNum = _max

        startRow += 1

    return maxNum


# matirx = [
#     [-1, -1, -1],
#     [-1, 2, 2],
#     [-1, -1, -1]
# ]
matrix = [
    [-90, 48, 78],
    [64, -40, 64],
    [-81, -7, 66]
]

r = solution(matrix)
print(r)
