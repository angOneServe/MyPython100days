import requests

#基本的get请求,返回HTTPresponse
respond=requests.get("https://www.cnblogs.com/mzc1997/p/7813801.html")
print(respond.status_code)#打印状态
