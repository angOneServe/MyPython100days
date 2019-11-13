from tkinter import *

win=Tk()

lable=Label(win,text="***")
lable.focus_set()
lable.pack()

win.bind("<Control-Up>",lambda e:print("ctrl+up"))

win.mainloop()
