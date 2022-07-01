arr = [8, 9, 6, 6, 5, 4, 3, 2, 1]


def partition(l, r, find):
    if l == r:
        return arr[l]
    x = arr[l]
    i = l
    j = r
    while i <= j:
        while arr[i] <= x and i <= j:
            i += 1
        while arr[j] > x and i <= j:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    sl = j - l
    # print(find,sl)
    # print(arr)
    if sl <= find:
        return partition(l, j, find)
    else:
        return partition(j, r, find - sl)
    # print(i,j)
    # return j


def solution(l, r, x):
    if l < r:
        mid = partition(l, r, x)
        solution(l, mid - 1, x)
        solution(mid + 1, r, x)

partition(0, len(arr) - 1, 7)
print(arr)
