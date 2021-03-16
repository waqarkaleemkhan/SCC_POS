from tkinter import *

class Categories():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Swat Cash and Carry System")
        self.root.config(bg="purple1")
        title=Label(self.root,text="Adding Cadtegories",font=("times new roman",20,"bold"),bg="purple1",fg="white")
        title.pack(side=TOP,fill=X)

        categories_Name=Label(self.root,text="Category Name",font=("times new roman",16,"bold"),fg="white",bg="purple1").place(x=20,y=60)
        self.txt_category_Name=Entry(self.root,font=("times new roman",15))
        self.txt_category_Name.place(x=190,y=60)

        btn_add_category=Button(text='Save',bg="skyblue",fg="white",font=("times new roman",16)).place(x=185,y=130,width=210)
root=Tk()
obj=Categories(root)
root.mainloop()