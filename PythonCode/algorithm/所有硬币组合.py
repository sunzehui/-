#     1,5,10,25 组合出100元有多少中方案

def countWays(n, coins, cur):
    if cur == 0:
        return 1
    i = 0
    res = 0
    while n >= i * coins[cur]:
        res += countWays(n-coins[cur]*i, coins, cur - 1)
        i += 1
    return res


def solution(N):
    return countWays(N, [1, 5, 10, 25], 3)


r = solution(100)
print(r)
