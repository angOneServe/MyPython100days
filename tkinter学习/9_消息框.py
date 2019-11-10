from tkinter import *
from  tkinter.messagebox import *
#信息提示
showinfo("消息提示","这是一个消息框的测试例子")
#警告提示
showwarning("警告提示","这是一个警报")
#错误提示
showerror("错误提示","这是一个错误")
#确认与取消
sign=askokcancel("确认与取消","确认进入是否消息框，取消进入询问消息框?")
if not sign:
    s=askquestion("询问消息框","是否启动三消息对话框？")
    if s:
        taan=askyesnocancel()
        print(taan)#True False None
else:
    askyesno("是否消息框","是否消息框")
