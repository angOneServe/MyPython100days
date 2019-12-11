from imp import reload
import day16_20.reload_plugin
import time
while True:
    time.sleep(1)
    #import day16_20.reload_plugin              #不可以动态重载代码文件

    m=reload(day16_20.reload_plugin)             #可以动态重载代码文件，需要先import
    c=m.C()
    c.say()


    #with open("../reload_plugin.py","r") as f:  #可以动态重载代码文件,不需要import，需要打开文件
    #    exec(f.read())

    #f=open("../reload_plugin.py","r").read()
    #eval(f)        SyntaxError: invalid syntax


