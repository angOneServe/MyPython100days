from tkinter import *
#窗口创建
win=Tk()

'''
<Shift_L>       左shift键
<Shift_R>       右shift键
<F5>            
<Return>        回车键
<Backspace>     返回键
a
'''

b=Label(win,text="***")
b.focus_set()
b.pack()

b.bind("<Shift_L>",lambda e:print("左shift键"))
b.bind("<Shift_R>",lambda e:print("右shift键"))
b.bind("<F5>",lambda e:print("f5"))
b.bind("<Return>",lambda e:print("回车"))
b.bind("<BackSpace>",lambda e:print("退格"))
b.bind("a",lambda e:print("a"))
b.bind("A",lambda e:print("A"))
#事件循环
win.mainloop()
