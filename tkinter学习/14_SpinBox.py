#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")

def update():
    print(spinbox.get())
    print(v)
v=StringVar()
'''
from_=0,        从哪里开始
to=100,         到哪里结束
increment=5,    步长
textvariable=v, 一个字符，不知道干啥的
command=update  监听方法
'''
spinbox=Spinbox(win,from_=0,to=100,increment=-1,textvariable=v,command=update)
spinbox.pack()

#事件循环
win.mainloop()
