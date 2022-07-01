# 描述：如果一个字符串恰好包含2个h、1个i和1个o，我们就称这个字符串是hiho字符串
# 输入
# happyhahaiohell
# 输出
# 5



def checkChar(c):
    return c == 'h' or c == 'i' or c == 'o'

def endCheck(arr,i,j):
    x, y, z = 0, 0, 0
    for i in range(i, j+1):
        if arr[i] == 'h':
            x += 1
        elif arr[i] == "i":
            y += 1
        elif arr[i] == "o":
            z += 1
    return x == 2 and y == 1 and z == 1


def checkArr(arr, i, j):
    x, y, z = 0, 0, 0
    for i in range(i, j+1):
        if arr[i] == 'h':
            x += 1
        elif arr[i] == "i":
            y += 1
        elif arr[i] == "o":
            z += 1
    return x >= 2 and y >= 1 and z >= 1


def solution(s):
    i, j = 0, -1
    count = 9999999

    for i in range(len(s)):
        if not checkChar(s[i]):
            continue
        if j == -1:
            j = i + 1
        while j < len(s):
            if checkChar(s[j]) and checkArr(s, i, j):
                if count > j - i + 1 and endCheck(s,i,j):
                    count = j - i + 1
                break
            j += 1

    return count


r = solution("happyhahaiohell")
print(r)
