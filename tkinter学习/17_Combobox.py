#导入tkinter
from tkinter import *
from tkinter import ttk
#窗口创建
win = Tk()
win.title("Combobox")


#下拉控件
cv=StringVar()

cm=ttk.Combobox(win,textvariable=cv)
cm.pack()
cm["value"]=("滨江","吉林","辽宁")

cm.current(0)

#绑定事件
def func(e):
    print(cm.get())
    print(cv.get())

cm.bind("<<ComboboxSelected>>",func)
#事件循环
win.mainloop()
