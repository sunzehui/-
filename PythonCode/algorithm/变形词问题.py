# 如果a字符串经过变换之后和b字符串相同，即为变形词

a = "abdc"
b = "cbca"


def solution(a, b):
    helper = [0] * 128
    for i, v in enumerate(a):
        helper[ord(v)] += 1
    for i,v in enumerate(b):
        helper[ord(v)] -=1
    for i,v in enumerate(helper):
        if v!=0:
            return False
    return True
r= solution(a,b)
print(r)
