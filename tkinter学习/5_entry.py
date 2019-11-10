from tkinter import *
#主窗口
win=Tk()
win.title("Entry测试 -窗口")
win.geometry("100x100+0+0")
#密码输入框
entry1=Entry(win,show="x")
entry1.pack()
#接收文本
entryText=Variable()
entry2=Entry(win,textvariable=entryText)
entry2.pack()
#用一个变量【tkinter.Variable】代替entry接收输入的数据
entryText.set("haha")
print(entryText.get())
win.mainloop()

