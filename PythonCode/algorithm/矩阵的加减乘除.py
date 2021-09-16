matrixA = [
    [1, 0, 2],
    [-1, 3, 1]
]
matrixB = [
    [3, 1],
    [2, 1],
    [1, 0]
]


def matrixMultiply(a, b):
    am = len(a)
    an = len(a[0])
    bn = len(b[0])
    result = [[0] * bn for i in range(am)]
    print(result)
    for i in range(am):
        for j in range(bn):
            for k in range(an):
                result[i][j] += a[i][k] * b[k][j]
    showMatrix(result)


def matrixSubtraction(a, b):
    M = len(a)
    N = len(a[0])
    result = [[0] * N for i in range(M)]
    for i in range(M):
        for j in range(N):
            result[i][j] = a[i][j] - b[i][j]
    showMatrix(result)


def showMatrix(matrix):
    s = ""
    for m in matrix:
        s += " ".join(map(str, m))
        s += "\n"
    print(s)


# matrixSubtraction(matrixA, matrixB)
matrixMultiply(matrixA, matrixB)
