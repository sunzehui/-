# import math
#
# num = 5
# count = 0
# length = math.floor(math.log2(num)) + 1
# for i in range(0, length):
#     r = num & (1 << i)
#     count += 1 if r != 0 else 0
# print(count)

# 第二种解法
# num = 5
# count = 0
# while num != 0:
#     count += 1
#     # (x - 1) & x 的效果：消掉最低位的1
#     num = num - 1 & num
# print(count)

def lowbit(x):
    return -x & x


N = 29
x = N
cnt = 0
while x != 0:
    x -= lowbit(x)
    print(x)
    cnt += 1
print(cnt)
