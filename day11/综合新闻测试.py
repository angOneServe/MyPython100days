import urllib.request as request
import json
respond=request.urlopen("http://api.tianapi.com/generalnews/?key=cd18d691dd680a80fafe3855a4e2c9a5&num=20&page=1&rand=1")
jsonText=respond.read().decode("utf-8")
news=json.loads(jsonText)["newslist"]
for new in news:
    print(new["ctime"])
    print(new["title"])
    print(new["description"])
    print(new["picUrl"])
    print(new["url"])
