#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")

'''
<B1-Motion>
<B2-Motion>
<B3-Motion>
'''

win.bind("<B1-Motion>",lambda e:print("鼠标左键移动"))
#事件循环
win.mainloop()
