# 给定一个N*N的矩阵matrix，在这个矩阵中，只有0和1两种值，
# 返回边框全是1的最大正方形的边长长度
# 0 1 1 1 1
# 0 1 0 0 1
# 0 1 0 0 1
# 0 1 1 1 1
# 0 1 0 1 1
# 返回4
def solution(arr):
    n = 5
    N = 5
    while n > 0:
        for i in range(0, n):
            if i + n > N:
                break
            for j in range(0, n):
                row = i
                col = j
                isBreak = False
                if i + n > N:
                    break

                # 从左往右
                while col < j + n:
                    col += 1
                    if arr[row][col-1] == 0:
                        isBreak = True
                        break
                if isBreak:
                    break
                col -= 1

                print(col)
                # 从上往下
                while row < i + n:
                    row += 1
                    if arr[row-1][col] == 0:
                        isBreak = True
                        break
                if isBreak:
                    break
                row -= 1
                # 从右往左
                while col >= j:
                    col -= 1
                    if arr[row][col+1] == 0:
                        isBreak = True
                        break
                if isBreak:
                    break
                col += 1
                # 从下往上
                while row >= i:
                    row -= 1
                    if arr[row+1][col] == 0:
                        isBreak = True
                        break
                if isBreak:
                    break
                row += 1
                return n

        n -= 1


matrix = [
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 1, 1]
]

r = solution(matrix)
print(r)
