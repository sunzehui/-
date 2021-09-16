arr = [1, 3, 8, 8,9]


def bSearch(x):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = l + r >> 1
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return r


print(bSearch(3))
