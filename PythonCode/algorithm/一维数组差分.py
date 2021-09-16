# 给定一个数组，求对arr[l]~arr[r]中的每个元素+c，输出数组
l, r = 2, 5
N = 1000
arr = [0,1, 2, 3, 4, 5, 6, 7, 8, 9] + [0] * N
n = 9
c = 2
b = [0] * N
print(arr)

def insert(l, r, c):
    b[l] += c
    b[r + 1] -= c


def solution():
    # 先对求出差分数组，再将做一次insert，然后利用前缀和还原
    for i in range(1, n + 1):
        insert(i, i, arr[i])

    for i in range(1, n + 1):
        insert(l, r, c)
    for i in range(1, n + 1):
        b[i] += b[i - 1]
    print(b)


solution()
