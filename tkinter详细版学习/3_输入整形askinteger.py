#导入tkinter
from tkinter import *
from tkinter import simpledialog
#窗口创建
win = Tk()
win.title("")

ask=simpledialog.askinteger("整数录入","请输入整数",initialvalue=0)

print(ask.keys())
#事件循环
win.mainloop()
