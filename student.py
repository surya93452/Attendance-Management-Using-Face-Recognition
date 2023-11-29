from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student")
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        #bg imag
        img3=Image.open(r"C:\Users\sura\Desktop\CIP Project\s.png")
        img3=img3.resize((1550,800),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=125,y=200,width=1275,height=460)
        #left label Frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",11,"bold"))
        left_frame.place(x=0,y=1,width=630,height=460)
        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",11,"bold"))
        current_course_frame.place(x=5,y=20,width=610,height=110)        
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",11,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer Science Engineering","IT","Mechanical","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=3,pady=5,sticky=W)
        
        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",11,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",11,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","B.E","B.Tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=3,pady=5,sticky=W)        
        
        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",11,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",11,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Select Semester",font=("times new roman",11,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=2,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",11,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Semester - I","Semester - II")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)       
        

        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",11,"bold"))
        class_student_frame.place(x=5,y=130,width=610,height=400)        

        #STUDENT ID 
        studentid_label=Label(class_student_frame,text="Student ID:",font=("times new roman",11,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=2,sticky=W)
       
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",11,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,sticky=W)    
        
        #STUDENT NAME 
        studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",11,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=2,pady=2,sticky=W)
       
        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",11,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Class Division 
        class_div_label=Label(class_student_frame,text="Section:",font=("times new roman",11,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=2,pady=2,sticky=W)
       
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",11,"bold"),state="readonly",width=18)
        div_combo["values"]=("S1","S2","S3","S4")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,stick=W)
        
        # Roll no
        roll_no_label=Label(class_student_frame,text="Roll no:",font=("times new roman",11,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=2,pady=2,sticky=W)
       
        roll_no_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",11,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",11,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=2,pady=2,sticky=W)
       
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",11,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,stick=W)
        
        # dob
        dob_label=Label(class_student_frame,text="D.O.B:",font=("times new roman",11,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=2,pady=2,sticky=W)
       
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",11,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        # Email
        email_label=Label(class_student_frame,text="E Mail:",font=("times new roman",11,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=2,pady=2,sticky=W)
       
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",11,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        # Phone no
        phone_no_label=Label(class_student_frame,text="Phone no:",font=("times new roman",11,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=2,pady=2,sticky=W)
       
        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",11,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        # Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",11,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=2,pady=2,sticky=W)
       
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",11,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        # Teacher name
        teacher_label=Label(class_student_frame,text="Teacher:",font=("times new roman",11,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=2,pady=2,sticky=W)
       
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",11,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        # Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #Button Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=190,width=630,height=500)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=630,height=60)
        
        take_phot_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=60,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_phot_btn.grid(row=0,column=0)
        
        
        #Right label Frame        
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",11,"bold"))
        right_frame.place(x=635,y=1,width=637,height=460)
        
        #====================================Search System=================================================

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",11,"bold"))
        search_frame.place(x=5,y=20,width=620,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",11,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=2,pady=2,sticky=W)
        #search
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial",11,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)
        
        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky="W")

        search_btn=Button(search_frame,text="Search",command=self.search_data,width=13,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)
        
        showall_btn=Button(search_frame,text="Show All",command=self.fetch_data,width=13,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=2)
        
        #====================Table Frame==================
        
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=90,width=620,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]='headings'
        
        
        self.student_table.column("dep",width=200)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=200)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
    
#====================function declaration====================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields must be filled",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(
                    host="127.0.0.1",username="root",password="surya@93452",database="face_recognition"
                    )
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                
                                                                                                                                self.var_dep.get(),
                                                                                                                                self.var_course.get(),
                                                                                                                                self.var_year.get(),
                                                                                                                                self.var_semester.get(),
                                                                                                                                self.va_std_id.get(),
                                                                                                                                self.var_std_name.get(),
                                                                                                                                self.var_div.get(), 
                                                                                                                                self.var_roll.get(), 
                                                                                                                                self.var_gender.get(), 
                                                                                                                                self.var_dob.get(), 
                                                                                                                                self.var_email.get(), 
                                                                                                                                self.var_phone.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_teacher.get(),
                                                                                                                                self.var_radio1.get()
                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 

            
    #===============fetch data==============
    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student order by Name asc")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        #=================get cursor=========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    # uodate function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields must be filled",parent=self.root)
                                                                                                                                                                                        
        else:
            try:
                Upadate=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)                                                                                                                                                                                    
                if Upadate>0:
                    conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                    self.var_dep.get(),                                       
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.va_std_id.get()
                                                                                                                                                                                ))
                else:
                    if not Upadate:
                        return                                                                                                                                       
                messagebox.showinfo("success","student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
        
    #delete function 
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","student id must be required",parent=self.root) 
        else:
            try:
                delete=messagebox.askyesno("Student Delete","Do you want to delete student",parent=self.root)       
                if delete>0:
                    conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
        
        
    def reset_data(self):
        self.var_dep.set("Select Department")   
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
        
    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","please select option")
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where"+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"'%")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
        
        
    #===========generate data set or take photo samples===============
    def generate_dataset(self):    
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields must be filled",parent=self.root)                                                                                                                                                                               
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                    self.var_dep.get(),                                       
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.va_std_id.get()==id+1,
                                                                                                                                                                                ))      
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #======== load predefined data on face frontals from opencv==============
                
                face_classifier=cv2.CascadeClassifier("C:\\Users\\sura\\Desktop\\CIP Project\\haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==300:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                      


            #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","please select option")
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="surya@93452",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()