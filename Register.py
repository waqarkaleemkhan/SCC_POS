from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
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
        txt_fname=Entry(frame1,font=("times new roman",15),bg="light gray").place(x=50,y=130,width=250)

        last_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        txt_lname=Entry(frame1,font=("times new roman",15),bg="light gray").place(x=370,y=130,width=250)

        contact=Label(frame1,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        txt_contact=Entry(frame1,font=("times new roman",15),bg="light gray").place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        txt_email=Entry(frame1,font=("times new roman",15),bg="light gray").place(x=370,y=200,width=250)

        question=Label(frame1,text="Securtiy Qustion",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        cmb_quest['values']=("Select","Your first pet name","Your Birth Place","Your Best Friend Name")
        cmb_quest.place(x=50,y=270,width=250)
        cmb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        txt_answer=Entry(frame1,font=("times new roman",15),bg="light gray").place(x=370,y=270,width=250)

        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        txt_password=Entry(frame1,font=("times new roman",15),bg="light gray").place(x=50,y=340,width=250)

        conform_password=Label(frame1,text="Conform Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        txt_conform_password=Entry(frame1,font=("times new roman",15),bg="light gray").place(x=370,y=340,width=250)


        chk=Checkbutton(frame1,text="I Agree The Terms and Conditions",onvalue=1,offvalue=0,font=("Times new roman",12),bg="white").place(x=50,y=380)

        btn=Button(frame1,text="Register",font=("times new roman",15),bg="purple1").place(x=50,y=420,width=250)
        btn_login=Button(self.root,text="Login",font=("times new roman",15),bg="purple1",cursor="hand2").place(x=150,y=510,width=250)
root=Tk()
obj=Register(root)
root.mainloop()