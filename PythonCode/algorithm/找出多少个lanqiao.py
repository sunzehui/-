matrix = [
    "SLANQIAO",
    "ZOEXCCGB",
    "MOAYWKHI",
    "BCCIPLJQ",
    "SLANQIAO",
    "RSFWFNYA",
    "XIFZVWAL",
    "COAIQNAL"
]

m = len(matrix)
n = len(matrix[0])
dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]
s = "LANQIAO"


def check(x, y):
    cnt = 0
    for i, j in dirs:
        ok = True
        for k in range(1, 7):
            nexti = x + i * k
            nextj = y + j * k
            if nexti >= m or nextj >= n or matrix[nexti][nextj] != s[k]:
                ok = False
                break
        if ok:
            cnt += 1
    return cnt


# check(1, 1)
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "L":
            count += check(i, j)
print(count)
