def helper(n, arr, cur):
    newArr = []
    if cur == 0:
        nil = []
        first = [arr[0]]
        newArr.append(nil)
        newArr.append(first)
        return newArr
    oldArr = helper(n, arr, cur - 1)

    for i in oldArr:
        newArr.append(i)
        _temp = i.copy()
        _temp.append(arr[cur])
        newArr.append(_temp)

    return newArr


def solution(N):
    arr = helper(N, [1,2,3], N - 1)
    return arr

r = solution(3)
print(len(r))
print(r)
