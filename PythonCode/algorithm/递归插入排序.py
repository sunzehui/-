arr = [5, 4, 3, 2, 1]


def insert_sort(arr, k):
    if k == 1:
        return arr
    insert_sort(arr, k - 1)
    # 当前k是第二个
    if arr[k - 2] > arr[k - 1]:
        # 如果：第0个大，第1个小，则让第0个向后移动
        # 保存第1个的数据
        temp = arr[k - 1]
        i = k - 2
        # 保证下标遍历到最前面的一个，且只移动比第一个小的
        while i >= 0 and arr[i] > temp:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = temp


insert_sort(arr, len(arr))

print(arr)
