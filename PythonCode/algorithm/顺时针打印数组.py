# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10



def printArr(arr):
    # 行指针和列指针
    r, c = 0, 0
    # 边界
    rowWall = len(arr) - 1
    colWall = len(arr[0]) - 1
    # 循环走圈，直到指针和边界交叉
    while c <= colWall and r <= rowWall:
        # 复制一份
        leftUpRow, leftUpCol = r, c
        # 从左往右，直到左指针碰到墙
        while leftUpCol <= colWall:
            print(arr[leftUpRow][leftUpCol], end=" ")
            leftUpCol += 1
        # 指针回退到数组范围内，为下次迭代做准备
        leftUpCol = colWall
        # 已经走过的在下一次跳过
        leftUpRow += 1


        while leftUpRow <= colWall:
            print(arr[leftUpRow][leftUpCol], end=" ")
            leftUpRow += 1
        leftUpRow = rowWall
        leftUpCol -= 1

        while leftUpCol >= c:
            print(arr[leftUpRow][leftUpCol], end=" ")
            leftUpCol -= 1
        leftUpRow -= 1
        leftUpCol = c

        while leftUpRow > r:
            print(arr[leftUpRow][leftUpCol], end=" ")
            leftUpRow -= 1

        r += 1
        c += 1
        rowWall -= 1
        colWall -= 1


arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
printArr(arr)
