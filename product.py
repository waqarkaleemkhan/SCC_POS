from tkinter import *
import psycopg2

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
        #right frame named detail frame

        detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="purple1")
        detail_Frame.place(x=500,y=40,width=850,height=560)




root=Tk()
obj=Product(root)
root.mainloop()