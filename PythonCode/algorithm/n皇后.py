def timmer(func):
    import time
    # 传入的参数是一个函数
    def deco(*args, **kwargs):
        print('函数：{_funcname_}开始运行：'.format(_funcname_=func.__name__))
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('函数:{_funcname_}运行了 {_time_}秒'
              .format(_funcname_=func.__name__, _time_=round(end_time - start_time, 2)))
        return res

    return deco

N = 12
cnt = 0
rec = [0] * N
res = []


def printArr(arr, N):
    for i in arr:
        j = 0
        while j < N:
            if j == i:
                print("1", end=" ")
            else:
                print("0", end=" ")
            j += 1
        print()


def solution(row):
    global cnt
    if row == N:
        cnt += 1
        res.append(rec.copy())
        return
    for col in range(0, N):
        isOk = True
        for i in range(0, row):
            # 该列是否有皇后      副对角线（右上-左下）是否有皇后   正对角线（左上-右下）是否有皇后
            if rec[i] == col or i + rec[i] == row + col or rec[i] - i == col - row:
                isOk = False
                break
        if isOk:
            rec[row] = col
            solution(row + 1)
            rec[row] = 0

@timmer
def all():
    solution(0)
    #
    # for i in res:
    #     printArr(i, N)
    #     print("-" * 8)
all()
