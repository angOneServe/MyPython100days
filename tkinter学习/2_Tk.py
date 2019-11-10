from tkinter import *
from threading import Thread

#利用线程创建窗口
class myWin(Tk):
    def __init__(self,name,x,y,sign=False):
        super().__init__()
        self.sWidth=self.winfo_screenwidth()    #需要主线程调用winfo_screenwidth  winfo_screenheight
        self.sHeight=self.winfo_screenheight()
        self.thread=Thread(target=self.buildWin,args=(name,x,y,sign,self.sWidth,self.sHeight))
        self.thread.start()

    def buildWin(self,name,x,y,sign,sw,sh):

        self.win=Tk()
        self.win.title(name)
        #设置大小
        if sign:
            self.win.geometry(f"{x}x{y}+{int((sw-x)/2)}+{int((sh-y)/2)}")
        else:
            self.win.geometry(f"50x30+{x}+{y}")

        #设置最大化大小 最小化大小
        self.win.minsize(0,0)
        self.win.maxsize(500,500)
        #事件循环检测
        self.win.mainloop()



for x in range(0,200,100):
    for y in range(0,120,60):
        myWin(f"我的第{x/50}{y/30}个窗口",x,y)


myWin(f"我的第{300}{300}个窗口",300,300,True)
