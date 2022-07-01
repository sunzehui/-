arr = [9, 8, 2, 6, 5, 4, 3, 2, 1]


def partition(arr, start, end):
    Pivot = arr[start]
    lp = start + 1
    rp = end
    while lp <= rp:
        # 如果左指针小于主元，左指针向右移动
        if arr[lp] <= Pivot:
            lp += 1
        else:
            # 如果大于主元，左指针和右指针对应元素交换位置，右指针向左移动
            arr[rp], arr[lp] = arr[lp], arr[rp]
            rp -= 1
    # 将最后的空位填上主元
    arr[start], arr[rp] = arr[rp], arr[start]

    return rp


def quickSort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        # 递归左序列
        quickSort(arr, start, p - 1)
        # 递归右序列
        quickSort(arr, p + 1, end)


quickSort(arr, 0, len(arr)-1)
print(arr)

