#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")

#expand是否居中显示[为True时side无效]
#fill 是否填充x y both
l_base=Label(win,text="win",bg="red").pack(expand=True,fill=BOTH)

l1=Label(l_base,text="l1",bg="blue") #理论上是一样显示结果是以l_base为父控件开始布局，但是事实上跟父控件是win的
l1.pack(expand=True,fill=BOTH)

l2=Label(l1,text="l2",bg="green")
l2.pack(expand=True,fill=BOTH)


import time
l2.pack(in_=l_base)

l3=Label(l2,text="l3",bg="white")
l3.pack(expand=True,fill=X)

l4=Label(l2,text="l4",bg="black",fg="white")
l4.pack(expand=False,side=LEFT,before=l3)



#列表方式返回所有子控件对象
for v in win.slaves():
    print(v["text"])
l4.forget()#将控件隐藏，并且忽略原有设置，之后用pack将其显示



#事件循环
win.mainloop()
