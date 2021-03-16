from tkinter import *
import psycopg2
from tkinter import messagebox

DB_NAME = "SCC_POS" 
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = "root"





conn = psycopg2.connect(database=DB_NAME,user=DB_USER,host=DB_HOST,port=DB_PORT,password=DB_PASS)
print('database connected')
my_cursor=conn.cursor()
my_cursor.execute("""CREATE TABLE IF NOT EXISTS categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255)
	)""")
conn.commit()

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

        btn_add_category=Button(text='Save',command=self.save_category,bg="skyblue",fg="white",font=("times new roman",16)).place(x=185,y=130,width=210)


    def save_category(self):
        if self.txt_category_Name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                my_cursor.execute("insert into categories(category_name) value(%s)",
                (
                    self.txt_category_Name.get()
                ))
                conn.commit()
                messagebox.showinfo("Success","Category is added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}")

root=Tk()
obj=Categories(root)
root.mainloop()