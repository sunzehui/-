arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l, r = 4, 6
N = len(arr)
dp = [0] * N
for i in range(0, len(arr)):
    dp[i] = dp[i - 1] + arr[i]

print(dp)
res = dp[r] - dp[l - 1]
print(res)
