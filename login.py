from tkinter import*
from datetime import *
import time
from PIL import Image,ImageTk,ImageDraw
from math import*
class Clock():
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        #labels for background colors
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        #frames
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="Login Here",font=("times new roman",20,"bold"),bg="white",fg="purple1").place(x=250,y=50)
        
        #email field
        email=Label(login_frame,text="Email Address",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="light gray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        #Password field
        password=Label(login_frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_password=Entry(login_frame,font=("times new roman",15),bg="light gray")
        self.txt_password.place(x=250,y=280,width=350,height=35)


        #rgister button
        rgister_btn=Button(login_frame,text='For New Account Register Here',font=("times new roman",12),bg="white",fg="#B00857",bd=0,cursor="hand2").place(x=243,y=320)

        login_btn=Button(login_frame,text='Login Here',font=("times new roman",15),bg="purple1",fg="white",cursor="hand2").place(x=250,y=370,width=250)


        #label to place the clock image
        self.lbl=Label(self.root,text="\nSwat Cash And Carry",font=("Book Antiqua",15,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        # self.clock_image()
        self.working_clock()
    def clock_image(self,hr,min_,sec_):
        #for clock Image
        clock=Image.new("RGB",(400,400),(8,25,35)) #create new empty image first size secod color
        draw=ImageDraw.Draw(clock) # draw new image
        bg=Image.open("images/cl.jpg") # open the image downloaded
        bg=bg.resize((300,300),Image.ANTIALIAS) # size th image use ANTIALIAS for not breaking pixles
        clock.paste(bg,(50,50))#paste the image on new image which is create
        
        # for hour line image
        #           x1,y1,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #for min line image
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="purple",width=3)
        #for sec line
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        #for circle in center
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("images/clock_new.png")#save the image

    def working_clock(self):
        hour=datetime.now().time().hour
        minutes=datetime.now().time().minute
        seconds=datetime.now().time().second
        hr=(hour/12)*360
        min_=(minutes/60)*360
        sec_=(seconds/60)*360
        self.clock_image(hr,min_,sec_)

        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working_clock)
        

root=Tk()
obj=Clock(root)
root.mainloop()