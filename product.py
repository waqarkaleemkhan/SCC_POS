from tkinter import *

class Product():
    def __init__(self,root):
        self.root=root
        self.root.title("Swat Cash and Carry")
        self.root.geometry("1650x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Swat Cash and Carry System",font=("times new roman",20,"bold"),bg="purple1",fg="white")
        title.pack(side=TOP,fill=X)

        # left frame named manage frame
        manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="purple1")
        manage_Frame.place(x=20,y=40,width=450,height=560)
        
        manage_Title=Label(manage_Frame,text="Manage Products",bg="purple1",fg="white",font=("times new roman",20,"bold"))
        manage_Title.grid(row=0,columnspan=2,pady=20)
        #right frame named detail frame

        detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="purple1")
        detail_Frame.place(x=500,y=40,width=850,height=560)




root=Tk()
obj=Product(root)
root.mainloop()