def countSort(arr):
    # 寻找最大值k，开辟k+1个空间，因为下标多出来个0
    k = max(arr)
    helper = [0] * (k + 1)
    # 遍历一遍数据，将数值和helper的索引对应起来，helper值代表数量
    for v in arr:
        helper[v] += 1
    # 从0号位置开始回填数据
    cur = 0
    for i in range(0, len(helper)):
        while helper[i] > 0:
            arr[cur] = i
            cur += 1
            helper[i] -= 1


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
countSort(arr)
print(arr)
