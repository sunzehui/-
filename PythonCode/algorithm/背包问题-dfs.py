weight = [1, 2, 3, 2]
value = [3, 2, 4, 2]
N = len(weight)
BagW = 5


def dfs(bag, index):
    if bag <= 0:
        return 0
    if index == N:
        return 0
    v1 = dfs(bag, index+1)
    if bag >= weight[index]:
        v2 = value[index] + dfs(bag - weight[index], index + 1)
        return max(v1, v2)
    else:
        return v1


def solution():
    ans = dfs(BagW, 0)
    print(ans)
solution()
