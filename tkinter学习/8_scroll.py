from tkinter import *

#创建窗口
win=Tk()
win.title("Scrollbar 测试窗口")

#创建滚动条
scroll=Scrollbar(orient=HORIZONTAL)

text=Text(win,width=30,height=10,borderwidth=50,insertbackground="red",highlightcolor="green",insertofftime=200,insertontime=200,insertwidth=10,selectbackground="yellow",selectborderwidth=20,undo=True)
#side放到窗体的一侧，fill填充
scroll.pack(side=BOTTOM,fill=X)
#关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

text.pack()

str1="文 字".center(400,"*")
text.insert(INSERT,str1)

win.mainloop()
