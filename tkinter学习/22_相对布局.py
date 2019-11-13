#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")

Label(win,text="111",bg="blue").pack(fill=X,side=TOP)
Label(win,text="222",bg="blue").pack(fill=Y,side=TOP)
Label(win,text="333",bg="blue").pack(fill=X,side=TOP)
#事件循环
win.mainloop()
