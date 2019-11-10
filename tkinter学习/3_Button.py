from tkinter import *
import time
from threading import Thread
#自定义函数[线程启动改变按键状态]

def ChangeButton(bt,s):
    b1["state"]="disable"
    b1.pack()
    time.sleep(s)
    b1["state"]="normal"
    b1.pack()
#创建窗口
win=Tk()
win.title("测试按键的使用--窗口")
win.geometry("100x100+20+10")

#创建按键
def Func():
    print("按键点击")
b1=Button(win,text="按键1",command=Func,bg="grey",fg="white",activebackground="black")
b1.pack()
t=Thread(target=ChangeButton,args=(b1,5))
t.start()
#事件循环
win.mainloop()
