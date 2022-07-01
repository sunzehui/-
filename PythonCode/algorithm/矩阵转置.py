n = int(input())
m = int(input())
# 创建二维数组
arr = [[0] * m for i in range(0, n)]
# enumerate每次循环可以得到下表及元素
for i in range(0, n):
    line = input().split()
    for j, v in enumerate(line):
        arr[i][j] = v

for i in range(0, m):
    for j in range(0, n):
        print(arr[j][i] + " ", end="")
    print()
