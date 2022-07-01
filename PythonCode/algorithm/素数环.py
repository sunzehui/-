N = 6
rec = [0] * N
rec[0] = 1


def check(num, i):
    return i not in rec and isP(rec[num - 1] + i)


def isP(n):
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def solution(num):
    if num == N and isP(rec[N - 1] + rec[0]):
        print(rec)
        return
    for i in range(2, N + 1):
        # 检查下一个数字能不能符合要求，不能就继续下一个，可以就把该数字记录
        if check(num, i):
            rec[num] = i
            solution(num + 1)
            # 所有数字都不合适就回溯
            rec[num] = 0


solution(1)
