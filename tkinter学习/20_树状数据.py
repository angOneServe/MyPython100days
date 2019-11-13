#导入tkinter
from tkinter import *
from tkinter import ttk
#窗口创建
win = Tk()
win.title("")

#树状数据
tree=ttk.Treeview(win)
tree.pack()

#添加一级树枝
treef1=tree.insert("",0,text="中国",values=("f1"))
treef2=tree.insert("",1,text="美国",values=("f2"))
treef3=tree.insert("",2,text="英国",values=("f3"))

#添加二级树枝
treef1_1=tree.insert(treef1,0,text="江西",values=("f1_1"))
treef1_2=tree.insert(treef1,1,text="广东",value=("f1_2"))


#添加三级树枝
treef1_2_1=tree.insert(treef1_2,0,text="广州",values=("f1_2_1"))
treef1_2_2=tree.insert(treef1_2,0,text="珠海",values=("f1_2_2"))
treef1_2_3=tree.insert(treef1_2,0,text="深圳",values=("f1_2_3"))
#事件循环
win.mainloop()
