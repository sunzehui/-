arr = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
]
height = len(arr)
width = len(arr[0])

prefix = [
    [0 for j in range(width + 1)] for i in range(height + 1)
]
for i in range(height):
    for j in range(width):
        # 矩阵前缀和 = 上一个行值+上一个列值-左上角值+当前值
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]

x1, y1, x2, y2 = 2, 2, 4, 4
# 矩阵和 = 前缀和右下角 - 左边矩阵和 - 上边矩阵和 + 左上角矩阵和
ret = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
print(ret)
