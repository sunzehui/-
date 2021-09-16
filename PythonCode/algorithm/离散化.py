# 求第2到第4的值
arr = [0] * 1000
insert = [(1, 2), (3, 6), (7, 5)]
query = [(1, 3), (4, 6), (7, 8)]
alls = []
s = [0]*1000

def find(x):
    l, r = 0, len(alls) - 1
    while l < r:
        mid = l + r >> 1
        if alls[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return r+1


def solution(arr,alls):
    # 将所有下标离散化
    for i,v in insert:
        alls.append(i)
    for i,v in query:
        alls.append(i)
        alls.append(v)

    # 排序加去重
    alls.sort()
    alls = list(set(alls))
    print(alls)
    # 累加
    for i,v in insert:
        x = find(i)
        arr[x] += v
    # 处理前缀和
    for i in range(1, len(alls)+1):
        s[i] = s[i-1]+arr[i]

    # 处理询问
    for i,v in query:
        l = find(i)
        r = find(v)
        print(s[r]-s[l-1])


solution(arr,alls)
