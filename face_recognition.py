from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import cv2 
from time import strftime
from datetime import datetime
import winsound



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=2,width=1450,height=40)
        
        
        bgimg=Image.open(r"C:\Users\sura\Desktop\CIP Project\mi (1).jpg")
        self.photobgimg=ImageTk.PhotoImage(bgimg)
        
        
        f_lbl=Label(self.root,image=self.photobgimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)
    
        b1_1=Button(self.root,text="FACE RECOGNITION",cursor="hand2",command=self.face_recog,font=("times new roman",30,"bold"),bg="purple",fg="white")
        b1_1.place(x=500,y=380,width=600,height=60)
        
    #===================attendance===========
       
        
    def mark_attendance(self, i, r, n, d):
        self.current_date = datetime.now().strftime('%Y-%m-%d')
    # Connect to MySQL database
        db = mysql.connector.connect(host="127.0.0.1",user="root",password="surya@93452",database="face_recognition")
        cursor = db.cursor()

    # Check if the name already exists in the database
        cursor.execute("SELECT name FROM attendance")
        result = cursor.fetchall()
        name_list = [row[0] for row in result]
    
        if((i not in name_list)  and (r not in name_list)  and (n not in name_list)  and (d not in name_list)):
        # Insert the new attendance record into the database
            query = "INSERT INTO attendance (ID,RollNumber,Name,Department,Date,Time,Status) VALUES (%s, %s, %s,%s,%s,%s,%s)"
            values = (i, r, n, d, datetime.now().strftime('%d-%m-%Y'), datetime.now().strftime('%H:%M:%S'), 'Present')
            cursor.execute(query, values)
            db.commit()
    # Close the database connection
            db.close()

    

    #============================Face Recognition=============
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,recognizer):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=recognizer.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                                
                
                if confidence>81:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)                    
                    self.mark_attendance(i,r,n,d)

                    frequency = 1000  # Set Frequency to 2500 Hertz
                    duration = 500  # Set Duration to 1000 ms == 1 second
                    winsound.Beep(frequency, duration)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face detected",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    

                coord=[x,y,w,h]
                
            return coord

        def recognize(img,recognizer,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",recognizer)
            return img
        
        faceCascade=cv2.CascadeClassifier("C:\\Users\\sura\\Desktop\\CIP Project\\haarcascade_frontalface_default.xml")
        recognizer=cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        video_cap.set(cv2.CAP_PROP_FPS,120)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,recognizer,faceCascade)
            cv2.imshow("Welcome to face recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()       
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()

