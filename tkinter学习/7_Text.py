from tkinter import *
from threading import Thread
import time
from PIL import Image,ImageTk
#窗口
win=Tk()
win.title("text测试--窗口")
win.geometry("200x300+0+0")
#文本控件
text=Text(win,width=30,height=10)
text.pack()
text.insert(END,"123456789请将光标移动")#END表示插入在最后面

def Show():

    image1=Image.open("aa.jpg")
    photo1=ImageTk.PhotoImage(image1)
    text.image_create(END,image=photo1)
bt=Button(text,text="请点击",command=Show)
text.window_create(INSERT,window=bt)    #在text中插入按键
str1="插入的文字40".center(40,"*")
def Fuc():
    time.sleep(5)
    text.insert(INSERT,str1)        #INSERT表示插入在光标处
t=Thread(target=Fuc)
t.start()
#事件主循环
win.mainloop()
