arr = [9, 8, 7, 6, 5, 9, 3, 2, 1]

#
def merge(arr, start, mid, end):
    helpArr = arr[:]
    lp = start
    rp = mid + 1
    cur = start
    print(arr[:start],arr[end:])
    print(start,end)
    print("----")
    while lp <= mid and rp <= end:
        print(lp,rp)
        if helpArr[lp] <= helpArr[rp]:
            arr[cur] = helpArr[lp]
            cur += 1
            lp += 1
        else:
            arr[cur] = helpArr[rp]
            cur += 1
            rp += 1

    while lp <= mid:
        arr[cur] = helpArr[lp]
        cur += 1
        lp += 1


def mergeSort(arr, start, end):
    if start < end:
        mid = start + ((end - start) >> 1)
        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, start, mid, end)


mergeSort(arr, 0, len(arr) - 1)
print(arr)

# def merge(a, b):
#     c = []
#     h = j = 0
#     while j < len(a) and h < len(b):
#         if a[j] < b[h]:
#             c.append(a[j])
#             j += 1
#         else:
#             c.append(b[h])
#             h += 1
#     if j == len(a):
#         for i in b[h:]:
#             c.append(i)
#     else:
#         for i in a[j:]:
#             c.append(i)
#     return c
#
# def merge_sort(lists):
#     if len(lists) <= 1:
#         return lists
#     middle = len(lists)//2
#     left = merge_sort(lists[:middle])
#     right = merge_sort(lists[middle:])
#     return merge(left, right)
# print(merge_sort(arr))
