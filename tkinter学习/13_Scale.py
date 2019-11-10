#导入tkinter
from tkinter import *
from threading import Thread
#窗口创建
win = Tk()
win.title("")

Wint=0
Hint=0
def ChangeW(W):
    label.config(width=W)
    label.pack()
def ChangeH(H):
    label.config(height=H)
    label.pack()


label=Label(win,width=Wint,height=Hint,bg="green")
label.pack()

#通过scale改变lbale大小
wscale=Scale(win,from_=0,to=100,orient=HORIZONTAL,tickinterval=50,length=200,command=ChangeW)
print(wscale.keys())
wscale.pack(side=RIGHT)


hscale=Scale(win,from_=0,to=20,orient=VERTICAL,tickinterval=50,length=200,command=ChangeH)
hscale.pack(side=BOTTOM)

#事件循环
win.mainloop()
