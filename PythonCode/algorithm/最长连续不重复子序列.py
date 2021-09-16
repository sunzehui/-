arr = [1, 2, 2, 3, 5]
s = [0] * 1000


def solution(arr):
    i, j = 0, 0
    m = 0
    for i in range(len(arr)):
        # s[arr[i] += 1 表示新增一个元素
        s[arr[i]] += 1
        while s[arr[i]] > 1:
            # s[arr[j] -= 1 表示抛弃一个元素
            s[arr[j]] -= 1
            j += 1
        m = max(m, i - j + 1)
    return m


print(solution(arr))
