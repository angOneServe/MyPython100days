#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")

'''
<ButtonRelease-1> 释放鼠标左键
<ButtonRelease-2> 释放鼠标滑轮
<ButtonRelease-3> 释放鼠标右键
'''
l=Label(win,text="11",bg="red")
l.pack()
l.bind("<ButtonRelease-1>",lambda e:print(f"在{e.x_root}，{e.y_root}释放鼠标左键"))
#事件循环
win.mainloop()
