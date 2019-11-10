import urllib.request as request
import json
respond=request.urlopen("http://api.tianapi.com/bulletin/?key=cd18d691dd680a80fafe3855a4e2c9a5",)
jsontext=respond.read().decode("utf-8")
dict1=json.loads(jsontext)
newslist=dict1["newslist"]
for v in newslist:
    print(v)
    print(v["mtime"])
    print(v["title"])
    print(v["digest"])
    print(v["imgsrc"])
    print(v["url"])
    print(v["source"])
