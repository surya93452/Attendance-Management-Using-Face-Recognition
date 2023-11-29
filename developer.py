from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")
        
        title_lbl=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=2,width=1450,height=40)
        
        
        imgtop=Image.open(r"C:\Users\sura\Desktop\CIP Project\scsvmv.jpg")
        imgtop=imgtop.resize((720,130),Image.ANTIALIAS)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)
        
        
        f_lbl=Label(self.root,image=self.photoimgtop)
        f_lbl.place(x=0,y=55,width=1530,height=325)
        
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=100,y=0,width=500,height=550)
        
        #Developer Info
        
        dev_label=Label(main_frame,text="Developed by :",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="P V SRIRAM",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=100,y=40)
        
        dev_label=Label(main_frame,text="SURYA PRAKASH",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=100,y=80)
        
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()