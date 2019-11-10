from tkinter import *
def update():
    print(Iv.get())
#窗口创建
win=Tk()
#变量【一组单选框要绑定同一个变量，value值相同表示同一个选项】
Iv=IntVar()
#单选题
radio1=Radiobutton(win,text="one",value=1,variable=Iv,command=update)
radio1.pack()

radio2=Radiobutton(win,text="two",value=2,variable=Iv,command=update)
radio2.pack()
Iv=2
#事件循环
win.mainloop()
