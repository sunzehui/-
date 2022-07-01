def check(matrix,x,y,k):
    for i in range(0,9):
        if matrix[x][i] == str(k) :
            return False
        if matrix[i][y] == str(k):
            return False
    for i in range((x//3)*3,(x//3+1)*3):
        for j in range((y//3)*3,(y//3+1)*3):
            if matrix[i][j] == str(k):
                return False
    return True

def solution(matrix,x,y):
    if x==9:
        print(matrix)
        exit()
    if matrix[x][y] == '0':
        for i in range(1,10):
            if check(matrix,x,y,i):
                matrix[x][y] = str(i)
                solution(matrix,x+(y+1)//9,(y+1)%9)
        matrix[x][y] = '0'
    else:
        solution(matrix,x+(y+1)//9,(y+1)%9)
matrix = []
for i in range(0,9):
    inp = list(input())
    matrix.append(inp)

# print(matrix)
solution(matrix,0,0)
# 005300000
# 800000020
# 070010500
# 400005300
# 010070006
# 003200080
# 060500009
# 004000030
# 000009700
