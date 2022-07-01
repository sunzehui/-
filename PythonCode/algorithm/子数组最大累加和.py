# 给定一个数组arr ,返回子数组的最大累加和
# 例: arr=[1,-2,3,5,-2,6,-1];
# 所有的子数组中[3,5,-2,6]
# 可以累加出最大的和12 ,所以返回12
def solution(arr):
    sumNum = arr[0]
    # 维护一个最大值
    maxNum = sumNum
    for i in range(1, len(arr)):
        # 累加和比0大的时候继续累加
        if sumNum >= 0:
            sumNum += arr[i]
        else:
            # 累加和小于0，丢弃，从当前重新开始计算
            sumNum = arr[i]
        # 当前累加和大于最大值时更新最大值
        if sumNum > maxNum:
            maxNum = sumNum

    print(maxNum)


arr = [1, -2, 3, 5, -2, 6, -1]
solution(arr)
