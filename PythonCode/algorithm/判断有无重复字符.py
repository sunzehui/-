s = "abcd"


# 创建一个128大小的数组，索引对应ASCII码的128位，数值对应数量，大于0代表重复了
def solution(s):
    charArr = [0] * 128
    for i, v in enumerate(s):
        if charArr[ord(v)] > 0:
            return False
        charArr[ord(v)] += 1
    return True


print(solution(s))
