from tkinter import  *
#自定义函数获取字符
def GetStr():
    print(uv.get(),pv.get())
    Messagelabel.config(text=f"信息提示：\n用户名:{uv.get()}\n密码：{pv.get()}")
#主窗口
root=Tk()
root.title("用户与密码--窗口")
root.geometry("300x200+0+0")

#文字
userlabel=Label(root,text="用户名：")
passwordlabel=Label(root,text="密码：")
Messagelabel=Label(root,text="信息提示：无")

#输入框
uv=Variable()
pv=Variable()
userEntry=Entry(root,textvariable=uv)
passwordEntry=Entry(root,textvariable=pv,show="*")
#布局
userlabel.pack(anchor=NW)
userEntry.pack(anchor=NW)
passwordlabel.pack(anchor=NW)
passwordEntry.pack(anchor=NW)
Messagelabel.pack(anchor=NW)
#按键
enterButton=Button(root,text="确认",command=GetStr)
enterButton.pack(anchor="center")

root.mainloop()
