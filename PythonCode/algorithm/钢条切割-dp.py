# 给定一段长度为n英寸的钢条和一个价格表,求钢条切割方案,使得销售收益rn最大

N = 10
price = [1, 5, 8, 16, 10, 17, 17, 20, 24, 30]


def dp():
    dpArr = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            dpArr[i] = max(dpArr[i - j] + price[j - 1], dpArr[i])
    return dpArr.pop()


def solution():
    ans = dp()
    print(ans)


solution()
