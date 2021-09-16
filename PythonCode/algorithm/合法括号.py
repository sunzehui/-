# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
N = 3
res = []


def dfs(l, r, s):
    if r > l or l > N or r > N:
        return
    if l == N and r == N:
        res.append(s)
        return
    dfs(l + 1, r, s + "(")

    dfs(l, r + 1, s + ")")


dfs(0, 0, "")
print(res)
