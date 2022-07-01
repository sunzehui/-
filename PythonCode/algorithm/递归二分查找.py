def binary_search(arr, low, high, key):
    if low > high:
        return -1
    mid = low + ((high - low) >> 1)
    midVal = arr[mid]
    if midVal > key:
        # 左查找
        return binary_search(arr, low, mid - 1, key)
    elif midVal < key:
        # 右查找
        return binary_search(arr, mid + 1, high, key)
    else:
        return mid


# 已经排序好的数组
arr = [1, 2, 3, 4, 5,9]
r = binary_search(arr, 0, 6, 2)
print(r)
