from tkinter import *
#先创建一个窗口
root=Tk()
root.title("我的窗口")
root.geometry("400x100+20+20")

#创建label
label=Label(root,
            text="标签文本dafdsafsafsafsafdsafadsfsaffdsds",
            bg="grey",
            fg="black",
            width=90,
            height=60,
            wraplength=50,
            anchor="center")

#显示label
label.pack()
#窗口事件循环启动
root.mainloop()
