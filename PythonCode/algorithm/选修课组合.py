arr = ['微积分', '音乐', '烹饪', '设计']


def dfs(arr, helper):
    if len(helper) == 2:
        print(helper)
        return

    for i in range(len(arr)):
        # 划分子问题
        newArr = arr[i+1:]
        newHelper = helper+[arr[i]]
        dfs(newArr,newHelper)


def solution():
    N = len(arr)
    dfs(arr, [])

solution()
