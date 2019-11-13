#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")

'''
<Enter> 当鼠标进入控件时触发事件
<Leave> 当鼠标离开控件时触发事件
'''

win.bind("<Enter>",lambda e:print(f"鼠标从位置{e.x_root}，{e.y_root}进入窗口"))
win.bind("<Leave>",lambda e:print(f"鼠标从位置{e.x_root}，{e.y_root}离开窗口"))


#事件循环
win.mainloop()
