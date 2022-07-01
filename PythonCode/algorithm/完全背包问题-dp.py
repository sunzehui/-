class item:
    def __init__(self, w, v):
        self.weight = w
        self.value = v

    def __str__(self):
        return f"重{self.weight},值{self.value}"


def printArr(arr):
    for item in arr:
        print(item)


items = [
    item(w, v) for w, v in [(2, 3), (1, 2), (3, 4), (2, 2)]
]

bagWeight = 10


def solution():
    dp = [[0 for _ in range(0, bagWeight + 1)] for _ in range(0, len(items))]
    # 初始化
    for i in range(0, bagWeight + 1):
        if i >= items[0].weight:
            dp[0][i] = i // items[0].weight * items[0].value
        else:
            dp[0][i] = 0
    printArr(dp)
    for i in range(1, len(items)):
        for j in range(0, bagWeight + 1):
            if j >= items[i].weight:
                # 不选本次
                v1 = dp[i - 1][j]
                # 选本次物品和剩下最大
                v2 = items[i].value + dp[i][j - items[i].weight]
                dp[i][j] = max(v1, v2)
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]

r = solution()
print(r)
