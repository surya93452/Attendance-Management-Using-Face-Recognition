from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import webbrowser

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help")
        
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=2,width=1450,height=40)
        
        
        bgimg=Image.open(r"C:\Users\sura\Desktop\CIP Project\h.jpg")
        self.photobgimg=ImageTk.PhotoImage(bgimg)
        f_lbl=Label(self.root,image=self.photobgimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        
        
                
        dev_label=Label(f_lbl,text="Click Here to Contact us on Instagram",bg="white",fg="blue",cursor='hand2',font=("times new roman",50,"underline"))
        dev_label.place(x=300,y=350)
        
        dev_label.bind('<Button-1>',lambda x:webbrowser.open_new("https://instagram.com/surya._._.prakash?igshid=ZGUzMzM3NWJiOQ=="))
       

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()