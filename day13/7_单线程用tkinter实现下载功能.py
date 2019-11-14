from tkinter import *
import time
from tkinter import messagebox
def Download():
    time.sleep(10)
    messagebox.showinfo("下载窗口","下载任务完成")


def main():

    win=Tk()
    win.title("单线程下载")

    Button(win,text="下载",command=Download).pack()
    Button(win, text="关于", command=lambda : \
        messagebox.showinfo("信息","本程序用于测试。。")).pack()
    win.mainloop()

if __name__=="__main__":
    main()