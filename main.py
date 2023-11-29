import os
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

from face_recognition import Face_Recognition
from student import Student
from train import Train
from help import Help
from developer import Developer

class Face_Recognition_System:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition")

         
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sura\Desktop\CIP Project\mimg.png")
        
        lb_bg=Label(self.root,image=self.bg)
        lb_bg.place(x=0,y=0,relwidth=1,relheight=1)


        #student button
        img4=Image.open(r"C:\Users\sura\Desktop\CIP Project\students.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(lb_bg,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=300,y=250,width=150,height=150)

        b1_1=Button(lb_bg,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
        b1_1.place(x=300,y=380,width=150,height=40)

        #detect face button
        img5=Image.open(r"C:\Users\sura\Desktop\CIP Project\facedetectimg.jpeg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(lb_bg,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=680,y=250,width=150,height=150)

        b1_1=Button(lb_bg,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
        b1_1.place(x=680,y=380,width=150,height=40)


        #help button
        img7=Image.open(r"C:\Users\sura\Desktop\CIP Project\helpimg.png")
        img7=img7.resize((275,140),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(lb_bg,image=self.photoimg7,command=self.help_data,cursor="hand2")
        b1.place(x=1050,y=250,width=150,height=150)

        b1_1=Button(lb_bg,text="Help Desk",command=self.help_data,cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
        b1_1.place(x=1050,y=380,width=150,height=40)

        #train data button
        img8=Image.open(r"C:\Users\sura\Desktop\CIP Project\Trainimg.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(lb_bg,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=300,y=500,width=150,height=150)

        b1_1=Button(lb_bg,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
        b1_1.place(x=300,y=630,width=150,height=40)

        #photo button
        img9=Image.open(r"C:\Users\sura\Desktop\CIP Project\photosimg.jpeg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(lb_bg,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=680,y=500,width=150,height=150)

        b1_1=Button(lb_bg,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
        b1_1.place(x=680,y=630,width=150,height=40)


        #exit button
        img11=Image.open(r"C:\Users\sura\Desktop\CIP Project\exitimg.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(lb_bg,image=self.photoimg11,command=self.iExit,cursor="hand2")
        b1.place(x=1050,y=500,width=150,height=150)

        b1_1=Button(lb_bg,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
        b1_1.place(x=1050,y=630,width=150,height=40)


    def open_img(self):
            os.startfile(r"C:\Users\sura\Desktop\CIP Project\data")    
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
         #===============Function Buttons=====================\

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)



    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def help_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Help(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()