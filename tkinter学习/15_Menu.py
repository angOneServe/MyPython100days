#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")

#菜单条创建 菜单条与窗口绑定
menubar=Menu(win)
win.config(menu=menubar)

#创建一个菜单选项
menu1=Menu(menubar,tearoff=True)
#添加分割线
menu1.add_command(label="英语",command=lambda :print("英语"))
menu1.add_command(label="中文",command=lambda :print("中文"))
menu1.add_separator()
menu1.add_command(label="退出",command=lambda :win.quit())

menubar.add_cascade(label="语言",menu=menu1)
#事件循环
win.mainloop()
