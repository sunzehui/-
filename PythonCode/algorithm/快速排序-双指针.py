arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def partition(arr, start, end):
    sentry = arr[start]
    lp = start + 1
    rp = end
    while lp <= rp:
        # 左指针一直向右移动，直到该元素比哨兵大
        while lp <= rp and arr[lp] <= sentry: lp += 1
        # 右指针一直向右移动，直到该元素比哨兵小
        while lp <= rp and arr[rp] > sentry: rp -= 1
        if lp < rp:
            # 防止左指针越界，交换左右指针元素
            arr[lp], arr[rp] = arr[rp], arr[lp]
    # 将哨兵填在右指针区域
    arr[start], arr[rp] = arr[rp], arr[start]
    return rp


def quickSort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quickSort(arr, start, p - 1)
        quickSort(arr, p + 1, end)


quickSort(arr, 0, len(arr) - 1)
print(arr)
