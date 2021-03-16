from tkinter import *

class Categories():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Swat Cash and Carry System")
        self.root.config(bg="purple1")
        title=Label(self.root,text="Adding Cadtegories",font=("times new roman",20,"bold"),bg="purple1",fg="white")
        title.pack(side=TOP,fill=X)

root=Tk()
obj=Categories(root)
root.mainloop()