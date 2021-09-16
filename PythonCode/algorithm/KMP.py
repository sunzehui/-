def getNextArr(p):
    p_length = len(p)
    nextArr = [0] * p_length
    nextArr[0] = -1
    nextArr[1] = 0

    j = 1
    k = nextArr[j]

    while j < p_length - 1:
        if k < 0 or p[j] == p[k]:
            j += 1
            k += 1
            nextArr[j] = k
        else:
            k = nextArr[k]
    return nextArr


def match(s, p):
    i, j = 0, 0
    s_length = len(s)
    p_length = len(p)
    next = getNextArr(p)
    print(next)
    while i < s_length:
        if j == -1 or s[i] == p[j]:
            j += 1
            i += 1
        else:
            j = next[j]
        if j == p_length:
            return i-j


r = match("ABDSCCSCACSD", "ababcabaa")
print(r)
