#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")

Label(win,text="good",bg="blue").place(x=10,y=10)

Label(win,text="nice",bg="red").place(x=10,y=60)

Label(win,text="nice",bg="red").place(x=10,y=120)
#事件循环
win.mainloop()
