from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train data")
        
        

        
        
        bgimg=Image.open(r"C:\Users\sura\Desktop\CIP Project\t.jpg")
        self.photoimgtop=ImageTk.PhotoImage(bgimg)
        
        
        
        bg_lbl=Label(self.root,image=self.photoimgtop)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=380,width=600,height=60)
        
    
    def train_classifier(self):
        data_dir=("C:\\Users\\sura\\Desktop\\CIP Project\\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1]) 
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #================ train the classifier and save==================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")     
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()