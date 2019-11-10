import json

d1={
    "name":1,
    "persondict":
        {
            "小明":111,
            "小花":222
        }
}
#json.dumps是可以将一个字典对象转换为字符串返回
#json.loads是可以将一个字符串转换为字典返回
#json.dump(dictbject,FileObject) 是可以将一个字典转换为字符串，并且存入文件对象
#json.load(fileObject)是可以将一个文件对象其中的json文本直接转换成字典
#加了s的方法，自动完成了字符串到文件流这一步
with open("jsonTest.json","w") as f:
    json.dump(d1,f)
with open("jsonTest.json","r") as f:
    print(json.load(f))

with open("jsonTest.jsonStr","w") as f:
    f.write(json.dumps(d1))
with open("jsonTest.json","r") as f:
    print(json.loads(f.read()))

