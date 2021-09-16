import time
import requests
header = {':authority': 'lbapi-rk.chaoxing.com',
          ':method': 'POST',
          ':path': '/lb/part/like',
          ':scheme': 'https',
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8',
          'content-length': '297',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'origin': 'https://live-rk.chaoxing.com',
          'referer': 'https://live-rk.chaoxing.com/a/90113411?info=eyJ1aWQiOiI2NDc5NDYzNiIsIm5hbWUiOiLlrZnms73ovokiLCJhdmF0YXIiOiJodHRwczovL3Bob3RvLmNoYW94aW5nLmNvbS9wLzY0Nzk0NjM2XzgwIn0=&cxcode=xxsb3736&cxurl=https%3A%2F%2Fzhibo.chaoxing.com%2F6176603&isSuspendDoc=1&courseId=null',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-site',
          'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url = "https://lbapi-rk.chaoxing.com/lb/part/like"
data = {"id": "lb234212445880613888-"+str(int(time.time()))+"-001",
        "ext": '{"room":"234127531358343169","na":"孙泽辉","headimgurl":"https://photo.chaoxing.com/p/64794636_80","uid":"lb234212445880613888","role":"3"}',
        "ss": "234212445880613888"}
for i in range(1, 999):
    print(requests.post(url=url, data=data, json=header).text)
    time.sleep(1)
