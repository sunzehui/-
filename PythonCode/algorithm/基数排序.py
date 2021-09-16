arr = [9,8,7,6,5,4,3,2,1]

# 获取第d位数
def getBasicNum(elem, d):
    return elem // 10 ** (d - 1) % 10


def sort(bucket, arr, d):
    # 对每一位入桶操作
    for elem in arr:
        num = getBasicNum(elem, d)
        if num == 1:
            bucket[1].append(elem)
        elif num == 2:
            bucket[2].append(elem)
        elif num == 3:
            bucket[3].append(elem)
        elif num == 4:
            bucket[4].append(elem)
        elif num == 5:
            bucket[5].append(elem)
        elif num == 6:
            bucket[6].append(elem)
        elif num == 7:
            bucket[7].append(elem)
        elif num == 8:
            bucket[8].append(elem)
        elif num == 9:
            bucket[9].append(elem)
        elif num == 0:
            bucket[0].append(elem)

    # 出桶还原回去，继续入桶
    cur = 0
    for item_list in bucket:
        for j in item_list:
            arr[cur] = j
            cur += 1
        item_list.clear()


def radixSort(arr):
    # 建桶
    bucket = [[] for i in range(0, 10)]
    # 先算出多少位
    k = max(arr)
    d = 1
    _d = 1
    while k // 10 != 0:
        k //= 10
        d += 1
    while _d <= d:
        sort(bucket, arr, _d)
        _d += 1


radixSort(arr)
print(arr)
