import os
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from face_recognition import Face_Recognition
from student import Student
from train import Train
from help import Help
from main import Face_Recognition_System
import getpass

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\\Users\\sura\\Desktop\\CIP Project\\login.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)
        
        
        imgs=Image.open(r"C:\\Users\\sura\\Desktop\\CIP Project\\sm.jpeg")
        imgs=imgs.resize((100,100),Image.LANCZOS)
        self.photoimages=ImageTk.PhotoImage(imgs)
        lblimgs=Label(image=self.photoimages,bg="black",borderwidth=0)
        lblimgs.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)
        
        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #==========icon images=============
        img2=Image.open(r"C:\\Users\\sura\\Desktop\\CIP Project\\uimg.jpg")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"C:\\Users\\sura\\Desktop\\CIP Project\\pass.jpg")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)
        #loginbutton
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="white")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="white")
        registerbtn.place(x=16,y=350,width=160)
        
        #forgetpassbtn
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="white")
        registerbtn.place(x=10,y=370,width=160)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
            messagebox.showinfo("Success","Login Success")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from login where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Confirm Login ")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
#==================================reset password============
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()==" ":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()==" ":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value) 
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update login set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,Please Login new password",parent=self.root2)
                self.root2.destroy()
#=============================forgot password Window================

    def forgot_password_window(self):
        if self.txtuser.get()==" ":
            messagebox.showerror("Error","Please Enter the email address and password")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from login where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170")

                frame=Frame(self.root2,bg="white")
                frame.place(x=0,y=0,relwidth=1,relheight=1)  

                l=Label(self.root2,text="Forgot password",font=("times new roman",20,"bold"),fg="navyblue",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your date of birth","Your Favourite spot","Your pet name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

            

                btn=Button(self.root2,text="Reset",command=self.reset_pass,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="navyblue")
                btn.place(x=140,y=290)

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        #===============Variables==================
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #============bg image=================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sura\Pictures\Screenshots\Screenshot (36).png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #==========Left image===============
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sura\Pictures\Screenshots\Screenshot (36).png")
        left_lbl=Label(self.root,image=self.bg)
        left_lbl.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        #============main frame==========
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #=================Label and entry==============

        #-------------------row 1

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.txt_fname.place(x=50,y=130,width=250)

       

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #----------row 2
        contact=Label(frame,text="Contact Number",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #------------------row 3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your date of birth","Your Favourite spot","Your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #-----------row 4
        pswd=Label(frame,text="Password ",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #=============check button===========
        
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to the terms and conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #==================buttons============
        
        #reg button
        b1_1=Button(frame,text="Register Now",command=self.register,cursor="hand2",font=("times new roman",20,"bold"),bg="green",fg="white")
        b1_1.place(x=10,y=430,width=300,height=40)

        b2_2=Button(frame,text="Login Now",command=self.return_login,cursor="hand2",font=("times new roman",20,"bold"),bg="green",fg="white")
        b2_2.place(x=330,y=430,width=300,height=40)

        # =======================Function Declaration===========
    def register(self):
        if self.var_fname.get()==" "  or self.var_email.get()==" "  or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required!")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree to our terms and conditions")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from login where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,Please try with another email")
            else:
                my_cursor.execute("insert into login values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()

                                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registred Successfully")
    def return_login(self):
        self.root.destroy()

    
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
    main()