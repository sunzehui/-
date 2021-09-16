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
arr = [[0 for i in range(N)] for _ in range(N)]
col = [False] * (N * 5)
dg = [False] * (N * 5)
udg = [False] * (N*5)


def dfs(n):
    if N == n:
        # print(arr)
        return
    for i in range(0, N):
        if not col[i] and not dg[n + i] and not udg[N - n + i]:
            col[i] = True
            dg[n + i] = True
            udg[N - n + i] = True
            arr[n][i] = "Q"

            dfs(n + 1)

            arr[n][i] = 0
            udg[N - n + i] = False
            dg[n + i] = False
            col[i] = False


@timmer
def all():
    dfs(0)
all()
