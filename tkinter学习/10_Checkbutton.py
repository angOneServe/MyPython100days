from tkinter import *
#创建主窗口
win=Tk()
win.title("Checkbutton 窗口")

#文本显示
v=Variable()
t1=Text(win,width=30,height=1,bg="red")
t1.insert(INSERT,"DSDSAD")
t1.delete(0.0,END)
t1.pack()

#更新
def update():
    message=""

    if hobby4.get()==True:
        hobby1.set(True)
        hobby2.set(True)
        hobby3.set(True)

    if hobby1.get()==True:
        message+="money,"
    if hobby2.get()==True:
        message+="power,"
    if hobby3.get()==True:
        message+="people,"
    t1.delete(0.0,END)
    t1.insert(END,message)
#checkbutton绑定的布尔变量
hobby1=BooleanVar()
check1=Checkbutton(win,text="money",variable=hobby1,command=update)
check1.pack()

hobby2=BooleanVar()
check2=Checkbutton(win,text="power",variable=hobby2,command=update)
check2.pack()

hobby3=BooleanVar()
check3=Checkbutton(win,text="people",variable=hobby3,command=update)
check3.pack()

hobby4=BooleanVar()
check4=Checkbutton(win,text="all",variable=hobby4,command=update)
check4.pack()
#事件循环
win.mainloop()
