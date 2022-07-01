inp = "4 85  3 234 45 345 345 122 30 12"
arr = list(map(int, inp.split()))


def selectSort(arr):
    cur = 0
    end = len(arr)
    while cur < end:
        minIndex = cur
        for i in range(cur, len(arr)):
            if arr[minIndex]>arr[i]:
                minIndex = i
        arr[cur], arr[minIndex] = arr[minIndex], arr[cur]
        cur +=1
selectSort(arr)
print(arr)
