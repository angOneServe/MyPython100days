from tkinter import *
import sys
class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

        self.myExit=Button(self)
        self.myExit["text"]="退出"
        self.myExit["fg"]="green"
        self.myExit["command"]=self.showText
        self.myExit.pack({"side":"left"})

        #重新更新配置
        self.myExit.config(height=5,cursor="",width=10,fg="yellow",bg="black",activeforeground="red",activebackground="green")



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def showText(self,text="退出"):
        self.T=Label(self)
        self.T["text"]=text
        self.T["fg"]="yellow"
        self.T["height"]=5
        self.T["width"]=10
        self.T["bg"]="black"
        self.T["bd"]=5
        print(self.T.keys())
        self.T["activebackground"]="blue"
        self.T["highlightthickness"]=10
        self.T.pack({"side":"bottom"})
        self.T["cursor"]="clock"
        self.T["state"]="active"

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
