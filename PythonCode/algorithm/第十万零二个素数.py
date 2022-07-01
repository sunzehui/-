import math
import time


def timmer(func):
    # 传入的参数是一个函数
    def deco(*args, **kwargs):
        print('函数：{_funcname_}开始运行：'.format(_funcname_=func.__name__))
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('函数:{_funcname_}运行了 {_time_}秒'
              .format(_funcname_=func.__name__, _time_=round(end_time - start_time,2)))
        return res

    return deco


@timmer
def solution(N):
    length = 2
    while (length / math.log(length)) < N:
        length += 1
    arr = [0] * length
    x = 2
    while x < length:
        if arr[x] != 0:
            x += 1
            continue
        k = 2
        while x * k < length:
            arr[x * k] = -1
            k += 1
        x += 1
    index = 0
    for i in range(2, len(arr)):
        if arr[i] == 0:
            index += 1
        if index == N:
            return i


r = solution(100000)
print(r)
