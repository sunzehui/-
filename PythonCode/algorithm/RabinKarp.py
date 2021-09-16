seed = 31


def hash(c):
    res = 0
    for i in range(len(c)):
        res = ord(c[i]) + res * seed
    return res


def hashArr(s, p):
    p_length = len(p)
    s_length = len(s)
    hashArr = [0] * s_length
    hashArr[0] = hash(s[0:p_length])

    i = p_length
    while s_length > i:
        startChar = s[i]
        endChar = s[i - p_length]
        _hash = seed * (hashArr[i - p_length] - ord(endChar) * seed ** (i - 1)) + ord(startChar)
        hashArr[i - p_length + 1] = _hash
        i += 1
    return hashArr


def searchSubstr(s, p):
    hash_p = hash(p)
    hashArray = hashArr(s, p)
    for i, v in enumerate(hashArray):
        if v == hash_p:
            print("match:", i)


s = "DABC"
searchSubstr(s, "AB")
