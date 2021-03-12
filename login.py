from tkinter import*
from PIL import Image,ImageTk,ImageDraw
class Clock():
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        title=Label(self.root,text="Login Page",font=("times new roman",50,"bold"),bg="#04444a",fg="white").place(x=0,y=50,relwidth=1)
        #label to place the clock image
        self.lbl=Label(self.root,bg="white")
        self.lbl.place(x=450,y=150,height=400,width=400)
        self.clock_image()
    def clock_image(self):
        #for clock Image
        clock=Image.new("RGB",(400,400),(255,255,255)) #create new empty image first size secod color
        draw=ImageDraw.Draw(clock) # draw new image
        bg=Image.open("images/cl.jpg") # open the image downloaded
        bg=bg.resize((300,300),Image.ANTIALIAS) # size th image use ANTIALIAS for not breaking pixles
        clock.paste(bg,(50,50))#paste the image on new image which is create
        
        # for hour line image
        draw.line((200,200,250,200),fill="black",width=3)
        #for min line image
        draw.line((200,200,280,210),fill="blue",width=3)
        #for sec line
        draw.line((200,200,300,240),fill="green",width=3)
        #for circle in center
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("clock_new.png")#save the image





root=Tk()
obj=Clock(root)
root.mainloop()