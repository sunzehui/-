def solution(N):
    allNum = [True] * (N + 1)
    allNum[0] = False
    allNum[1] = False
    nums = []
    for i in range(2, N + 1):
        if allNum[i]:
            nums.append(i)
            for j in range(i * i, N + 1, i):
                allNum[j] = False
    return nums


r = solution(100)
print(r)
print(len(r))
