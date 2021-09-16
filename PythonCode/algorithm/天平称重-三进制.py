# 天平称重: 变种3进制
# 用天平称重时, 我们希望用尽可能少的砝码组合称出尽可能多的重量。
# 如果有无限个砝码, 但它们的重量分别是1, 3, 9, 27, 81, ...
# 等3的指数幂神奇之处在于用它们的组合可以称出任意整数重量(砝码允许放在左右两个盘
# 中)。
# 本题目要求编程实现: 对用户给定的重量, 给出砝码组合方案, 重量 < 1000000。
# 例如：
# 用户输入：
# 5
# 程序输出：
# 9 - 3 - 1

def f(n, x):
    # n为待转换的十进制数，x为机制，取值为2-16
    b = []
    while True:
        s = n // x  # 商
        y = n % x  # 余数
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()
    return b

# 将输入的数字转成三进制
num = f(int(input()), 3)
# 倒序方便进位
num.reverse()
lis = []
print(num)
for i, v in enumerate(num):
    # 如果当前位数字是2，在头上插入-1
    if v == 2:
        lis.insert(0, -1)
        # 如果是最后一位就进一，不是就将原数组下一个位置自增1
        if i == len(num) - 1:
            lis.insert(0, 1)
        else:
            num[i + 1] += 1
    elif v == 3:
        # 如果最近两个都是2，进位导致变成3的时候
        # 头上插入0
        lis.insert(0, 0)

        if i == len(num) - 1:
            lis.insert(0, 1)
        else:
            num[i + 1] += 1
    else:
        # 0或1直接插入
        lis.insert(0, v)
res = [0] * len(lis)
for i, v in enumerate(lis):
    if v == 1:
        res[i] = 3 ** i
    elif v == -1:
        res[i] = -(3 ** i)
    else:
        pass
print(res)
