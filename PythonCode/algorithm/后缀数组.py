class shuf:
    def __init__(self, i, c):
        self.char = c
        self.index = i

    def __str__(self):
        return f"元素：{self.char}，下标：{self.index}"


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    while left <= right:
        if arr[left].char > pivot.char:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1
    arr[start], arr[right] = arr[right], arr[start]
    return right


def sortArr(arr, start, end):
    if end > start:
        p = partition(arr, start, end)
        sortArr(arr, start, p - 1)
        sortArr(arr, p + 1, end)


def getSubstrArray(s):
    subStrArray = []
    for i in range(len(s)):
        subStrArray.append(shuf(i, s[i:]))

    sortArr(subStrArray, 0, len(subStrArray) - 1)
    return subStrArray


def compareTo(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def solution(s, p):
    subStrArray = getSubstrArray(s)
    for i in subStrArray:
        print(i)
    l = 0
    r = len(s) - 1
    while r > l:
        mid = 1 + ((r + l) >> 1)
        midSuff = subStrArray[mid]

        if len(midSuff.char) >= len(p):
            compareFlag = compareTo(midSuff.char[0:len(p)], p)
        else:
            compareFlag = compareTo(midSuff.char, p)
        if compareFlag == 0:
            print(midSuff.index)
            break
        elif compareFlag < 0:
            l = mid+1
        else:
            r = mid-1


solution("ABABABABB", "BABB")
