import requests
import json
import time
import threading
import time
# import datetime
old_time = 1
new_time = 1
def change_time():
    global new_time
    global old_time
    new_time=old_time
    old_time=new_time-86400000

def get_time():

    t = time.time()

    #print(int(round(t * 1000)))  # 毫秒级时间戳
    #print(int(round(t * 1000))-86400000)
    # print(datetime.datetime.now())

    global new_time
    new_time = int(round(t * 1000))
    #new_time = 1582768983000
    
    dn = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(new_time/1000))
    # print(dn)

    global old_time
    old_time = new_time-86400000
    do = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(old_time/1000))
    print("\n\n\n"+do+'--'+str(dn)+"\n\n\n")
    # print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   #日期格式化




headers = {
    'cookie': 'lv=2; fid=6480; _uid=64794636; uf=fbe48ba271b0dbbdf47e9958ff4f2f3cd7b94c93cac0166c7e30f4aaa001d0c59deb4b84fe6f19fa1ab1561843d818eac49d67c0c30ca5047c5a963e85f11099217da90b4d805c4efd68be96b6183b1a95e54a2d0e600ba1f83ba7872499b7e40500d3ef8f86feb6; _d=1583930084186; UID=64794636; vc=63C1D826C6184D39AEA7A5575B7849CB; vc2=22D5A098A0B19FA63C318A04DF96B8F7; vc3=EQ79FNahLRbpICiEjQ3yrWVljLIF%2Fka9T8XTKnFkCpnt2yeqZ%2BGceCP3pvUt2uz%2BQ0l5Gfr8UO%2Bn2Iz6Z6NGsRWMdSEHHoPOsCYezammzrFkvhqoY3078QsM2%2Br2soWeeqBp0%2BTp%2BnpYmDc4TzA9F6ixIdtO%2B1sUsR8P%2Fh1PxZ4%3D98965584cf929e51b26a13e7c500b73e; xxtenc=dcca691b0b8df4db854ec9be407bc56e; DSSTASH_LOG=C_38-UN_5739-US_64794636-T_1583930084188; msign_dsr=1583996538541; search_uuid=6e017e02%2d9de4%2d462c%2d971f%2d5280bdd59a64; compiler-setting=211073345_16; thirdRegist=0; tl=1; _industry=6; route=dda7b098baa75826cda181090dfac97c; JSESSIONID=DA8A14057BC11BD252F4C753D1F14D8A.GroupTopic_WEB',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    'Host': 'groupweb.chaoxing.com',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "X-Requested-With": "XMLHttpRequest"
}


def request(old_date, new_date, value, headers):

    try:
        req = requests.get(url="https://groupweb.chaoxing.com/pc/topic/topiclist/b5208a734e214beabcc9747e5feebaf1/getTopicList?folder_uuid=&page=18&pageSize=20&kw=&last_reply_time=" +
                           str(old_date)+"&_="+str(new_date), headers=headers)
    except ConnectionResetError:
        print('error')
    j = json.loads(req.text)

    for data in j['datas']:
        try:
            req = requests.get(url="https://groupweb.chaoxing.com/pc/praise/" +
                               str(data['uuid'])+"/addTopicPraise?_="+str(value), headers=headers)
            
            req.keep_alive = False
            req.close()
        except:
            print("error")
        print(data['ftime']+data['content']+data['shareUrl'])
        value += 1
        msg = json.loads(req.text)
        while '频繁' in msg['msg']:
            
            print("频繁操作，延时10秒--线程1")
            time.sleep(10)
            req=requests.get(url="https://groupweb.chaoxing.com/pc/praise/" +
                               str(data['uuid'])+"/addTopicPraise?_="+str(value), headers=headers)
            if("频繁" not in req.text):
                msg['msg']="重试成功"
                break
            
        print(msg['msg']+"--线程1")
        #time.sleep(1)


value = 1584782268183
get_time()
print(old_time)
print(new_time)

while 1:
    change_time()
    request(old_time, new_time, value, headers)
