s = "ADC"


# 打印所有旋转词
def printAllSubstr(s):
    length = len(s)
    temp = ""
    for i in range(1, length + 1):
        temp = s[-i:] + s[:length - i]
        print(temp)


# 判断a是否可以旋转得到b
def solution(a, b):
    if len(a) != len(b):
        return False
    temp = b + b
    return a in temp


r = solution("ABC", "CAB")
print(r)
