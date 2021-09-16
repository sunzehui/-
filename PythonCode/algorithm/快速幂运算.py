# 快速幂运算
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


@timmer
def solution(x, n):
    pingfangshu = x
    result = 1
    while n:
        if n & 1 == 1:
            result *= pingfangshu
        pingfangshu *= pingfangshu
        n >>= 1
    return result


r = solution(2, 3)
print(r)
