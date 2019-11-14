from tkinter import *

#创建窗口
win=Tk()
win.geometry("300x300+0+0")

'''重要参数
master，父组件
bg,fg 背景/前景色
cursor，划过时的鼠标样式
postcommand,菜单打开时的回调方法
relief，边框样式sunken raised groove ridge
tearoff， 是否可撕下
tearoffcommand，撕下时的回调函数
title，撕下时的标题

'''

#菜单栏（）
menu_bar=Menu(win)
win.config(menu=menu_bar)

#子菜单
menup1=Menu(menu_bar,tearoff=True,title="File")
menup1.add_command(label="New Project...",command=lambda :print("New Project..."))
menup1.add_command(label="New ...",command=lambda :print("New ..."))
menup1.add_command(label="New scratch file...",command=lambda :print("New scratch file..."))
menup1.add_command(label="open",command=lambda :print("open"))

menup2=Menu(menu_bar,tearoff=True,title="Edit")
menup2.add_command(label="cut",command=lambda :print("cut"))
menup2.add_command(label="copy",command=lambda :print("copy"))

menup3=Menu(menu_bar,tearoff=False)
menup3.add_command(label="exit",command=lambda:win.quit())

#菜单栏添加子菜单
menu_bar.add_cascade(label="File",menu=menup1)
menu_bar.add_cascade(label="Edit",menu=menup2)
menu_bar.add_cascade(label="exit",menu=menup3)

#右键事件绑定
def ShowMenu1(event):
    menup1.post(event.x_root,event.y_root)
win.bind("<Button-1>",ShowMenu1)
def ShowMenu2(event):
    menu_bar.post(event.x_root,event.y_root)
win.bind("<Button-3>",ShowMenu2)
#窗口事件循环
win.mainloop()
