from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import psycopg2

DB_NAME = "SCC_POS" 
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = "root"





conn = psycopg2.connect(database=DB_NAME,user=DB_USER,host=DB_HOST,port=DB_PORT,password=DB_PASS)
print('database connected')
my_cursor=conn.cursor()
my_cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
	last_name VARCHAR(255),
    contact VARCHAR(20),
    email VARCHAR(255),
    question VARCHAR(50),
    answer VARCHAR(50),
    password VARCHAR(50),
    conform_password VARCHAR(50)
	)""")
conn.commit()

class Register():
    def __init__(self,root):
        self.root=root
        self.root.title("Swat Cash and Carry")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #background image
        self.bg=ImageTk.PhotoImage(file="images/pg.png")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        #left image
        self.left=ImageTk.PhotoImage(file="images/bg.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100)

        # Register Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="purple1").place(x=50,y=30)

        # input fields
        first_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_fname.place(x=50,y=130,width=250)

        last_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame1,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_email.place(x=370,y=200,width=250)

        question=Label(frame1,text="Securtiy Qustion",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Select","Your first pet name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_answer.place(x=370,y=270,width=250)

        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,show='*',font=("times new roman",15),bg="light gray")
        self.txt_password.place(x=50,y=340,width=250)

        conform_password=Label(frame1,text="Conform Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_conform_password=Entry(frame1,show='*',font=("times new roman",15),bg="light gray")
        self.txt_conform_password.place(x=370,y=340,width=250)

        self.var_chk=IntVar()
        self.chk=Checkbutton(frame1,text="I Agree The Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("Times new roman",12),bg="white").place(x=50,y=380)
        
        btn_register=Button(frame1,text="Register",command=self.register_data, font=("times new roman",15),bg="purple1").place(x=50,y=420,width=250)
        
        btn_login=Button(self.root,command=self.login_window,text="Login",font=("times new roman",15),bg="purple1",cursor="hand2").place(x=150,y=510,width=250)

    def clear_screen(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_conform_password.delete(0,END)
    
    def login_window(self):
        self.root.destroy()
        import login

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.txt_conform_password.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_conform_password.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif len(self.txt_password.get()) < 5:
            messagebox.showerror("Error","Password must be 6 digits or alphabits",parent=self.root)
            
        elif self.txt_password.get()!=self.txt_conform_password.get():
            messagebox.showerror("Error","Password is not same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Agree to out terms and conditions",parent=self.root)
        
        else:
            try:
                # sql_command="INSERT INTO users (first_name,last_name,contact,email,question,answer,password,conform_password) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                # values =(self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),self.txt_password.get(),self.txt_conform_password.get())
                # my_cursor.execute("select * from users where email=%s",self.txt_email.get())
                # row=my_cursor.fetchone()
                # print(row)
                # if row!=None:
                #     messagebox.showerror("Error","Email Already Exists",parent=self.root)
                # else:
                my_cursor.execute("select * from users where email=%s",(self.txt_email.get(),))
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Email Already Exists",parent=self.root)
                else:
                    my_cursor.execute("insert into users (first_name,last_name,contact,email,question,answer,password,conform_password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.cmb_quest.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get(),
                                        self.txt_conform_password.get()
                                        ))
                    conn.commit()
                
                    messagebox.showinfo("Success","Register Successfull",parent=self.root)
                    self.clear_screen()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
        


root=Tk()
obj=Register(root)
root.mainloop()