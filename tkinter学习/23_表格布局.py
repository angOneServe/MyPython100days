#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")
'''
表格布局会根据row的最大数，与column的最大数进行分配，自动调整布局
'''
Label(win,text="111").grid(row=0,column=0)
Label(win,text="222").grid(row=0,column=1)
Label(win,text="333").grid(row=0,column=3)
Label(win,text="dsdafdf").grid(row=1,column=0)
Label(win,text="wwdaw").grid(row=1,column=1)
Label(win,text="eede").grid(row=1,column=2)
#事件循环
win.mainloop()
