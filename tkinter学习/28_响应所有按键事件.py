#导入tkinter
from tkinter import *

#窗口创建
win = Tk()
win.title("")
'''
<Key>
响应所有键盘按键事件【需要让控件获得焦点focus_set】
'''
label1=Label(win,text="**",bg="red")
#设置焦点【】
label1.focus_set()
label1.pack()

label1.bind("<Key>",lambda e:print(f"按键对应的字符{e.char}\nkeycode[ascii码]{e.keycode}"))



#事件循环
win.mainloop()
