#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")

'''
Frame:
在桌面上显示一个矩形区域，作为控件容器
'''


#在frame上放置组件
frm1=Frame(win,bg="red")
frm1.pack(side=TOP)

Label(frm1,text="账号：").pack(side=LEFT)
tv1=StringVar()
Entry(frm1,textvariable=tv1).pack(side=RIGHT)

frm2=Frame(win,bg="green")
frm2.pack(side=TOP)

Label(frm2,text="密码：").pack(side=LEFT)
tv2=StringVar()
Entry(frm2,textvariable=tv2,show="*").pack(side=RIGHT)

Button(win,text="登录",command=lambda :print(f"账号{tv1.get()}\n密码{tv2.get()}\n登录")).pack(side=TOP)



#事件循环
win.mainloop()
