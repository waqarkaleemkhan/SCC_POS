from tkinter import *

class Product():
    def __init__(self,root):
        self.root=root
        self.root.title("Swat Cash and Carry")
        self.root.geometry("1650x700+0+0")




root=Tk()
obj=Product(root)
root.mainloop()