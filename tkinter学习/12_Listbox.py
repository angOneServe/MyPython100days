from tkinter import *
#窗口
win=Tk()
win.title("Listbox 窗口")


lb=Listbox(win,selectmode=BROWSE,bg="green",width=30,height=5)
lb.pack()
#插入
lb.insert(END,"11")
lb.insert(END,"22")
lb.insert(END,"33")
lb.insert(END,"44")

lb.insert(ACTIVE,"cool")
lb.insert(END,"11")
lb.insert(END,"22")
lb.insert(END,"33")
lb.insert(END,"44")

#删除
lb.delete(1,2)
#选中
lb.select_set(2,4)
#取消选中
lb.select_clear(2,2)

#返回当前的索引项
print(lb.curselection())

#判断一个选项是否被选中
print(lb.selection_includes(1))
#事件循环
win.mainloop()
