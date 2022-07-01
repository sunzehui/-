# 第K个数
arr = [9,8,7,6,5,4,3,2,1]
K = 7


def quick_sort(l, r, k):
    if l == r:
        return arr[l]
    x = arr[l]
    i = l
    j = r
    while i < j:
        while arr[i] < x:
            i += 1
        while arr[j] > x:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    sl = j - l + 1
    if k > sl:
        # 往右走
        return quick_sort(j + 1, r, k - sl)
    else:
        # 往左走
        return quick_sort(l, j, k)


r = quick_sort(0, len(arr) - 1, K)
print(r)
