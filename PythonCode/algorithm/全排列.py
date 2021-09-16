nums = range(1,10)
N = len(nums)
temp = [False] * N
stack = []

cnt = 0
def solution(index):
    if index == N:
        global cnt
        cnt+=1
        return
    for i in range(0, N):
        if temp[i]:
            continue
        temp[i] = True
        stack.append(nums[i])
        solution(index+1)
        temp[i] = False
        stack.pop()



solution(0)
print(cnt)
