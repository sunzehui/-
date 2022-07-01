# 有1元，5元，10元，50元，100元，500元的硬币
# 各3，2，1，3，0，2个
# 现在要用这些硬币支付620元，至少需要几枚硬币
money = [1, 5, 10, 50, 100, 500]
coins = [3, 2, 2, 3, 1, 2]
payMoney = 620


def solution(cur):
    global payMoney
    if payMoney <= 0:
        return 0
    if cur == 0:
        return payMoney
    # 当前张数加剩余组合
    cnt = min(payMoney // money[cur], coins[cur])
    payMoney -= cnt * money[cur]
    return cnt + solution(cur - 1)


r = solution(len(money) - 1)
print(r)
