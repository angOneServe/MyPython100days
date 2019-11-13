#导入tkinter
from tkinter import *
from tkinter import ttk
#窗口创建
win = Tk()
win.title("")

#表格数据
frmL=Frame(win).pack(side=LEFT)
tree=ttk.Treeview(frmL)
tree.pack()

tree["columns"]=("姓名","身高","年龄","体重")

tree.column("姓名",width=100)
tree.column("身高",width=100)
tree.column("年龄",width=100)
tree.column("体重",width=100)


#设置表头
tree.heading("姓名",text="姓名-name")
tree.heading("身高",text="身高-height")
tree.heading("年龄",text="年龄-age")
tree.heading("体重",text="体重-name")

#添加数据
tree.insert("",0,text="line1",value=("小真","177cm","23","70kg"))
tree.insert("",1,text="line2",value=("小da","157cm","26","60kg"))
#事件循环
win.mainloop()
