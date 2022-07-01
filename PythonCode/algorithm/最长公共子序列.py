s1 = "ADABEC"
s2 = "DBDCA"
m = len(s1)
n = len(s2)
# 用dp[i,j]表示S1i 和 S2j 的LCS的长度
dp = [[0 for i in range(m + 3)] for j in range(n + 3)]
import copy

p = copy.deepcopy(dp)
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i - 1] == s2[j - 1]:
            #            上一个位置最大+1
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            #           s1位置最大，s2位置最大取最大值
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[m][n])
