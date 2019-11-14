from tkinter import *
from tkinter import messagebox
from threading import Thread
import time
def Download_():
    time.sleep(5)
    messagebox.showinfo("下载窗口","下载完成")
def Download():
    Thread(target=Download_).start()
def ShowMessage_():
    messagebox.showinfo("关于", "本多线程程序用于测试")
def ShowMessage():
    Thread(target=ShowMessage_).start()
def main():
    win=Tk()
    win.title("多线程下载")

    Button(win,text="下载",command=Download).pack()
    Button(win, text="关于", command=ShowMessage).pack()

    win.mainloop()

if __name__=="__main__":
    main()