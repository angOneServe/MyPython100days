from time import time
from threading import Thread

import requests
url="http://api.tianapi.com/txapi/tenwhy/index"
'''
#get方式一，参数跟在后面
re=requests.get("http://api.tianapi.com/txapi/tenwhy/index?key=cd18d691dd680a80fafe3855a4e2c9a5&word=男子")
print(re.content)
#get方式二，参数单独加入
keys={
    "key":"cd18d691dd680a80fafe3855a4e2c9a5",
    "word":"男子"
}
re=requests.get(url,params=keys)
keys={
    "key":"cd18d691dd680a80fafe3855a4e2c9a5",
    "word":"男子"
}
print(re.content)
'''
keys={
    "key":"cd18d691dd680a80fafe3855a4e2c9a5",
}
re=requests.post(url=url,data=keys)
print(re.content.decode("utf-8"))



