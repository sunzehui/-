arr = [
    [1, 2, 6, 7],
    [3, 5, 8, 11],
    [4, 9, 10, 12]
]


def printArr(arr):
    res = []
    colWall = len(arr[0]) - 1
    rowWall = len(arr) - 1
    r, c = 0, 0
    # 是否从左往右打印
    l2r = True
    while r <= rowWall and c <= colWall:
        if l2r:
            res.append(arr[r][c])
            # 如果在顶行，只能向右走，然后掉头
            if r == 0 and c < colWall:
                c += 1
                l2r = not l2r
            # 在右边墙，向上走
            elif r > 0 and c == colWall:
                l2r = not l2r
                r += 1
            # 默认情况向右下角走
            else:
                r -= 1
                c += 1
        else:
            res.append(arr[r][c])
            if c == 0 and r < rowWall:
                l2r = not l2r
                r += 1
            elif r == rowWall:
                l2r = not l2r
                c += 1
            else:
                r += 1
                c -= 1

    print(res)


printArr(arr)
