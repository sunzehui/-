arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1):
            # 如果前者比后者大，就交换位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubbleSort(arr)
print(arr)
