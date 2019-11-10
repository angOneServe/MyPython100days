import time
#只写模式，不可读
with open("w文件.txt","w",encoding="utf-8") as f:
    f.write("aaaaa")
    #print(f.read()) #报错not readable
#可读可写
with open("w+文件.txt","w+",encoding="utf-8") as f:
    f.write("bbbbb")
    #没有seek的话，文件指针是在文件末尾的，直接read读取不到
    f.seek(0)#f.seek(以起始位置开始偏移多少,起始位置)a
    print(f.read())
#只读模式
with open("w+文件.txt","r",encoding="utf-8") as f:
    #f.writelines("ccccc")不可写
    print(f.read())
#可读可写
with open("w+文件.txt","r+",encoding="utf-8") as f:
    f.writelines("ddddd")
    f.seek(0)
    print(f.read())

#追加
with open("w+文件","at",encoding="utf-8") as f:#t，默认文本模式
    f.seek(0)
    f.truncate()    #清空内容
    f.write("e")
    #print(f.read())#not readable
with open("w+文件","a+",encoding="utf-8") as f:
    f.write("fffff")
    print("此时文件指针位置：",f.tell())
    f.seek(0)
    print(f.read())
#二进制文件 复制 图片藏视频压缩包
with open("drag.png","rb") as f:
    sprite=f.read()
    mp4f=open("test.zip","rb")
    mp4=mp4f.read()
    mp4f.close()
    with open("drag2.png","wb") as f2:
        f2.write(sprite)
        f2.write(mp4)

