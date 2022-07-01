k = int(input("输入K\n"))
arr = [0] * k


def heapify(arr, n, i):
    # 找到左孩子
    left = 2 * i + 1
    right = 2 * i + 2
    # 左边出界代表右边也出界了，return
    if left >= n:
        return
    # 寻找最大值
    max = left
    # 如果右边出界，则最大值是left
    if right >= n:
        max = left
    # 右边比左边大，最大值是右边
    elif arr[left] < arr[right]:
        max = right
    # 根节点比两节点最大的都大，直接return
    if arr[i] >= arr[max]:
        return
    # 交换位置，并对最大值下潜
    arr[i], arr[max] = arr[max], arr[i]
    heapify(arr, n, max)


def build_heap(arr):
    n = len(arr)
    lastNode = n - 1
    # 最后一个结点的父节点就是最底层有子节点的节点
    parent = (lastNode - 1) // 2
    # 默认从最底层有子节点的元素开始堆化
    for i in range(parent, -1, -1):
        heapify(arr, n, i)


def heapSort(arr):
    # 先堆化一下
    build_heap(arr)
    lastNode = len(arr) - 1
    # 将最后一个节点和堆化好的第一个节点（最大值）交换位置

    for i in range(lastNode, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


inp = input()
index = 0
while inp != '-1':
    print(index, k)
    if k > index:
        arr[index] = int(inp)

    elif index % k == 0:
        heapSort(arr)
        print(arr)
    elif k < index:
        print(arr[0],inp)
        if arr[0] < int(inp):
            arr[0] = int(inp)
            build_heap(arr)
    index += 1
    inp = input()
