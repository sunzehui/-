# 1-5 放在六个元素的数组中
arr = [1, 2, 3, 4, 5, 3]
result = 0
# 将数组里的所有数同1-5相异或
# 所以每个正常元素有两个，多出一个的元素会有3个
# A^A = 0 ; A^A^A = A
for i in range(1, 5+1):
    result = result ^ i
for i in arr:
    result ^= i

print(result)
