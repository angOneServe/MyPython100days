#导入tkinter
from tkinter import *
from tkinter import simpledialog
#窗口创建
win = Tk()
win.title("")

s=simpledialog.SimpleDialog(win,text="这里填写对话框要显示的文本",buttons=["按键一","button2","exit"])

#按键1返回0  按键2返回1。。。。
if s.go()==2:

    win.destroy()

#事件循环
win.mainloop()
