num = 6
a = num & 0x5555555  # 0101 0101 ... 0101
b = num & 0xaaaaaaaa  # 1010 1010 ... 1010
result = (a << 1) ^ (b >> 1)
print(result)
# 将num同0101... 和1010 进行与运算
# 再将a左移一位，b右移一位，两者异或
