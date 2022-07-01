triangle = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]


def solution(triangle):
    dp = [0] * len(triangle[-1])
    # 初始化
    for i in range(0, len(dp)):
        dp[i] = triangle[-1][i]

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(0, i + 1):
            dp[j] = triangle[i][j] + max(dp[j], dp[j + 1])
    return dp[0]


r = solution(triangle)
print(r)
