# Fibonacci数列的递推公式为: Fn=Fn-1+Fn- 2，其中F1=F2=1。
# 当n比较大时，FN也非常大，现在我们想知道，FN除以10007的余数是多少.
# 输入10，输出55

def rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return rec(n - 1) + rec(n - 2)


print(list(map(rec, range(1, 11))))
