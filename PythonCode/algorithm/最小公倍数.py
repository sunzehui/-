a, b = [5, 5]
max = a if a > b else b
count = 1
# 一不能算除数,包括最大值
for i in range(2, max+1):
    if a % i == 0 and b % i == 0:
        count = i
        break
print(a * b // count)
