arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def shellSort(arr):
    interval = len(arr) // 2
    while interval > 0:
        # 步长为4的插入排序
        for i in range(interval, len(arr)):
            temp = arr[i]
            k = i - interval
            while k >= 0 and temp < arr[k]:
                arr[k + interval] = arr[k]
                k -= interval
            arr[k + interval] = temp
        interval //= 2


shellSort(arr)
print(arr)
