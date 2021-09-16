arr = [1, 1, 2, 2, 3, 4, 3]
result = 0
# A^A = 0
for i in arr:
    result ^= i
print(result)
