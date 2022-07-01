arr = [-8, -4, -3, 0, 2, 4, 5, 8, 9, 10]


def solution(arr):
    l = 0
    end = len(arr) - 1
    r = end
    while l < r:
        if arr[r] + arr[l] < 10:
            # 二者加起来小于10，说明最大的和当前这个数加起来永远不可能等于10
            # 左指针右移，右指针回到原位
            l += 1
            r = end
        elif arr[r] + arr[l] > 10:
            # 二者加起来大于10，继续试下一个
            r -= 1
        else:
            # 两者等于10,打印,右指针回到原位,左指针继续扫描
            print(arr[l], arr[r])
            r = end
            l += 1


solution(arr)
