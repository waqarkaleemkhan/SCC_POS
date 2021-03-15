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
my_cursor.execute("""CREATE TABLE IF NOT EXISTS products(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
	product_price VARCHAR(255),
    product_quantity VARCHAR(50)
	)""")
conn.commit()


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
        
        product_Name=Label(manage_Frame,text="Product Name",font=("times new roman",16,"bold"),bg="purple1",fg="white").place(x=10,y=60)
        self.txt_product_Name=Entry(manage_Frame,font=("times new roman",15))
        self.txt_product_Name.place(x=170,y=60)

        product_Price=Label(manage_Frame,text="Product Price",font=("times new roman",16,"bold"),bg="purple1",fg="white").place(x=10,y=100)
        self.txt_product_Price=Entry(manage_Frame,font=("times new roman",15))
        self.txt_product_Price.place(x=170,y=100)

        product_Quantity=Label(manage_Frame,text="Product Qty",font=("times new roman",16,"bold"),bg="purple1",fg="white").place(x=10,y=140)
        self.txt_product_Quantity=Entry(manage_Frame,font=("times new roman",15))
        self.txt_product_Quantity.place(x=170,y=140)

        btn_Product_Save=Button(text='Save Product',command=self.save_product,bg="skyblue",fg="white",font=("times new roman",16)).place(x=40,y=250)
        #right frame named detail frame

        detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="purple1")
        detail_Frame.place(x=500,y=40,width=850,height=560)

    def clear_screen_product(self):
        self.txt_product_Name.delete(0,END),
        self.txt_product_Price.delete(0,END),
        self.txt_product_Quantity.delete(0,END)
    # saving product
    def save_product(self):
        if self.txt_product_Name.get()=="" or self.txt_product_Price.get()=="" or self.txt_product_Quantity.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        else:
            try:
                my_cursor.execute("insert into products(product_name,product_price,product_quantity) values(%s,%s,%s)",
                (self.txt_product_Name.get(),
                self.txt_product_Price.get(),
                self.txt_product_Quantity.get()

                ))
                conn.commit()
                messagebox.showinfo("Success","Product Add Successfully",parent=self.root)
                self.clear_screen_product()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)


root=Tk()
obj=Product(root)
root.mainloop()