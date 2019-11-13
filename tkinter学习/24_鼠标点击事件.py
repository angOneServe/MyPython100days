#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")

'''
<Button-1> 鼠标左键
<Button-2> 鼠标左键
<Button-3> 鼠标左键
<Double-Button-1> 鼠标双击左键
<Triple-Button-1> 鼠标三击左键

'''

#鼠标左键
win.bind("<Button-1>",lambda event:print(f"鼠标左键单击位置：{event.x_root},{event.y_root}"))
#鼠标左键双击
win.bind("<Double-Button-1>",lambda event:print(f"鼠标左键双击位置：{event.x_root},{event.y_root}"))
#鼠标滑轮双击
win.bind("<Double-Button-2>",lambda event:print(f"鼠标滑轮键双击位置：{event.x_root},{event.y_root}"))
#鼠标滑轮双击
win.bind("<Triple-Button-3>",lambda event:print(f"鼠标右键三击位置：{event.x_root},{event.y_root}"))
#事件循环
win.mainloop()
