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
        title=Label(self.root,text="Login Page",font=("times new roman",50,"bold"),bg="#04444a",fg="white").place(x=0,y=50,relwidth=1)
        #label to place the clock image
        self.lbl=Label(self.root,bg="white",bd=10,relief=RAISED)
        self.lbl.place(x=450,y=150,height=400,width=400)
        # self.clock_image()
        self.working_clock()
    def clock_image(self,hr,min_,sec_):
        #for clock Image
        clock=Image.new("RGB",(400,400),(255,255,255)) #create new empty image first size secod color
        draw=ImageDraw.Draw(clock) # draw new image
        bg=Image.open("images/cl.jpg") # open the image downloaded
        bg=bg.resize((300,300),Image.ANTIALIAS) # size th image use ANTIALIAS for not breaking pixles
        clock.paste(bg,(50,50))#paste the image on new image which is create
        
        # for hour line image
        #           x1,y1,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        #for min line image
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
        #for sec line
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=4)
        #for circle in center
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("clock_new.png")#save the image

    def working_clock(self):
        hour=datetime.now().time().hour
        minutes=datetime.now().time().minute
        seconds=datetime.now().time().second
        hr=(hour/12)*360
        min_=(minutes/60)*360
        sec_=(seconds/60)*360
        self.clock_image(hr,min_,sec_)

        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working_clock)
        

root=Tk()
obj=Clock(root)
root.mainloop()