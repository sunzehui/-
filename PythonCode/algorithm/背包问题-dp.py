weight = [2, 1, 3, 2]
value = [3, 2, 4, 2]
N = len(weight)
BagW = 5


# 从0-5的重量范围去取物品（在物品范围0-3中）
def dp():
    # 初始化第一行：
    dpArr = [[0 for _ in range(BagW + 1)] for _ in range(N)]
    for i in range(BagW + 1):
        if i >= weight[0]:
            dpArr[0][i] = value[0]
        else:
            dpArr[0][i] = 0

    # 剩余行 计算
    for i in range(N):
        for j in range(BagW + 1):
            # 要的起（剩余空间足够装下本轮编号物品）
            if j >= weight[i]:
                # 要本行的数据,需要将本行的价值和装上本行所剩下的空间所能够选到的最优解(也就是查表找历史最优解)
                v1 = value[i] + dpArr[i - 1][j - weight[i]]
                # 不要本行的数据,直接等于上一次不带本行的最优解
                v2 = dpArr[i - 1][j]
                # 当前行列数据 =  max(要本行的数值，不要本行的数值)
                dpArr[i][j] = max(v1, v2)
            else:
                # 要不起,等于上次不带本行的最优解
                dpArr[i][j] = dpArr[i - 1][j]
    # 返回最右下角的数据
    return dpArr[N - 1][BagW]


def solution():
    ans = dp()
    print(ans)


solution()
