# from cProfile import label
# from curses import A_HORIZONTAL
# from multiprocessing.sharedctypes import Value
# from re import L
# from sqlite3 import Cursor
# from turtle import heading, update
# from webbrowser import get
# from tkinter import font
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import*
import mysql.connector
 
class Employe:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1500x1080+0+0")
                self.root.title("Employee Management Syatem")

        ##------------------------------------VARIABLES-----------------------------------------------------------------##

                self.var_dep=StringVar()
                self.var_name=StringVar()
                self.var_desigination=StringVar()
                self.var_email=StringVar()
                # self.var_password =StringVar()
                self.var_address=StringVar()
                self.var_married=StringVar()
                self.var_dob=StringVar()
                self.var_doj=StringVar()
                self.var_Idproof=StringVar()
                self.var_Id_no=StringVar()
                self.var_gender=StringVar()
                self.var_phone=StringVar()
                self.var_country=StringVar()
                self.var_salary=StringVar()
                


        ##------------------------------------------TITLE NAME----------------------------------------------------------##
                label_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',28,'bold'),fg='red',bg="white")
                label_title=label_title.place(x=-30,y=0,width=1500,height=50)

        ## ----------------------------------------LOGO-------------------------------------------------------------------##
                # img_logo=Image.open('Image/emp.jpg')
                # img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
                # self.photo_logo=ImageTk.PhotoImage(img_logo)
        ##-------------------------- For Show Image On window use Label 'ya' bottom------------------------------------##
                # self.logo=Label(self.root,image=self.photo_logo).place(x=330,y=0,width=45,height=45)

        ##--------------------------------ImageFrame--------------------------------------------------------------------##
                # img_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white").place(x=0,y=45,width=1500,height=150)

        ###-----------------------------------1st--Image In Frame-----------------------------------------------------##  
                # self.img2=Label(self.root,image=self.photo2).place(x=0,y=48,width=280,height=145)

        ##----------------------------------2nd--Image In Frame--------------------------------------------------------##
                # img2=Image.open('Image/hmemp.jpg')
                # img2=img2.resize((280,143),Image.ANTIALIAS)
                # self.photo1=ImageTk.PhotoImage(img2)
                # self.logo=Label(self.root,image=self.photo1).place(x=282,y=49,width=280,height=143)

        ##-------------------------------------3rd--Image In Frame----------------------------------------------##        
                # img3=Image.open('Image/sem.png')
                # img3=img3.resize((280,144),Image.ANTIALIAS)
                # self.photo3=ImageTk.PhotoImage(img3)
                # self.logo=Label(self.root,image=self.photo3).place(x=562,y=48,width=280,height=144)
        ###--------------------------4th--Image In Frame--------------------------------------------------------------##
                # img4=Image.open('Image/Emprec.png')
                # img4=img4.resize((280,145),Image.ANTIALIAS)
                # self.photo4=ImageTk.PhotoImage(img4)
                # self.logo=Label(self.root,image=self.photo4).place(x=825,y=48,width=280,height=145)

        ##-------------------------5th--Image In Frame----------------------------------------------------------------##
                # img5=Image.open('Image/Empp.jpg')
                # img5=img5.resize((275,145),Image.ANTIALIAS)
                # self.photo5=ImageTk.PhotoImage(img5)
                # self.logo=Label(self.root,image=self.photo5).place(x=1095,y=48,width=275,height=145)


        ##------------------------------------------Main Frame Pic----------------------------------------------------##
                # img_main=Image.open('Image/sem.png')
                # img_main=img_main.resize((1370,515),Image.ANTIALIAS)
                # self.photo_mainimg_main=ImageTk.PhotoImage(img_main)
                # self.logo=Label(self.root,image=self.photo_mainimg_main).place(x=0,y=195,width=1370,height=515)

        ##--------------------------------Main Frame-------------------------------------------------------------------##
                Main_frame = Frame(self.root,bd=4,relief=RIDGE, bg="white").place(x=10,y=200,width=1345,height=496)

        ##--------------------------------Upper Frame in Main Frame --------------------------------------------------##
                Upper_frame =LabelFrame(Main_frame,bd=4,relief=RIDGE, bg="white",text="Employee Information",font=('times new roman',15,'bold'),fg='red').place(x=25,y=203,width=1315,height=252)

        #-------------------------------------------Labels And Field---------------------------------------------------##
                label_dep=Label(Upper_frame,text='Department    :',font=('Arial',11,'bold'),fg='black',bg='white')
                label_dep.place(x=42,y=230,width=120,height=22)

                combo_dep=ttk.Combobox(Upper_frame,textvariable=self.var_dep,font=('Arial',10,'bold'),width=25,state='readonly')
                combo_dep['value']=('Select Department','HR','Software Engineer','Manager','C.E.O','Adminstration','Accountant','Trainer')
                combo_dep.current(0)
                combo_dep.place(x=173,y=230,width=198,height=22)

        ##-------------------------------------------Name---------------------------------------------------------##
                label_name=Label(Upper_frame,text='Name                    :',font=('arial',11,'bold'),fg='black',bg='white')
                label_name.place(x=410,y=230,width=130,height=22)

                txt_name=ttk.Entry(Upper_frame,textvariable=self.var_name,font=('arial',10,'bold'),width=25)
                txt_name.place(x=560,y=230,width=198,height=22)

        ##------------------------------------------------Desigination :-----------------------------------------------##
                label_des=Label(Upper_frame,text='Desigination  :',font=('arial',11,'bold'),bg='white')
                label_des.place(x=43,y=250,width=120,height=50)

                label_des=ttk.Entry(Upper_frame,textvariable=self.var_desigination,width=25,font=('arial',10,'bold'))
                label_des.place(x=173,y=270,width=198,height=22)

        # ##----------------------------------------ADDRESS--------------------------------------------------------------##
                label_add=Label(Upper_frame,text='Address          :',font=('arial',11,'bold'),bg='white')
                label_add.place(x=42,y=299,width=120,height=22)

                label_add=ttk.Entry(Upper_frame,textvariable=self.var_address,width=25,font=('arial',10,'bold'))
                label_add.place(x=173,y=305,width=198,height=22)

        ##--------------------------------DOB---------------------------------------------------------------------------##
                label_dob=Label(Upper_frame,text='DOB                :',font=("arial",11,'bold'),bg='white')
                label_dob.place(x=42,y=340,width=120,height=22)

                label_dob=ttk.Entry(Upper_frame,textvariable=self.var_dob,width=25,font=('arial',10,'bold'))
                label_dob.place(x=173,y=340,width=198,height=22)

        ##-------------------------------------Select ID Proof-------------------------------------------------------##

                label_select_id_proof=Label(Upper_frame,text='ID Proof          :',font=("arial",11,'bold'),bg='white')
                label_select_id_proof.place(x=42,y=378,width=120,height=22)

                combo_select_id_proof=ttk.Combobox(Upper_frame,textvariable=self.var_Idproof,font=('Arial',10,'bold'),width=25,state='readonly')
                combo_select_id_proof['value']=('Select ID Proof ','Aadhar Card','Voter Card','Driving Licence','Bank Passbook','Passport','PAN Card','Picture')
                combo_select_id_proof.current(0)
                combo_select_id_proof.place(x=173,y=378,width=198,height=22)

        ##-------------------------------------ENTER ID NUMBER--------------------------------------------------------##
                label_Id_no=Label(Upper_frame,text='Enter ID No.         :',font=('arial',11,'bold'),bg='white')
                label_Id_no.place(x=410,y=378,width=130,height=22)

                label_select_id_proof=ttk.Entry(Upper_frame,textvariable=self.var_Id_no,width=25,font=('arial',10,'bold'))
                label_select_id_proof.place(x=560,y=378,width=198,height=22)

        ##------------------------------------------Email-ID-----------------------------------------------------------##
                label_email=Label(Upper_frame,text='Email ID                :',font=("arial",11,'bold'),bg='white')
                label_email.place(x=410,y=268,width=130,height=22)

                label_email=ttk.Entry(Upper_frame,textvariable=self.var_email,width=25,font=('arial',10,'bold'))
                label_email.place(x=560,y=268,width=198,height=22)


        ## password 
                # label_password = Label(Upper_frame, text="password  :", font =("arial", 11, 'bold'),bg ='white')
                # label_password.place(x=600,y =268,width=130,height=22) 

                # label_password = ttk.Entry(Upper_frame, textvariable=self.var_password, width =25,front=('arial',10,'bold'))
                # label_password.place(x=630,y = 268,width=198,height=22)

        ##----------------------------------------------Married Status-------------------------------------------------##
                label_married_status=Label(Upper_frame,text='Married Status    :',font=("arial",11,'bold'),bg='white')
                label_married_status.place(x=410,y=303,width=130,height=22)

                # label_married_status=ttk.Entry(Upper_frame,width=25,font=('arial',11,'bold'))

                combo_married_status=ttk.Combobox(Upper_frame,textvariable=self.var_married,font=('Arial',10,'bold'),width=25,state='readonly')
                combo_married_status['value']=('Select','Unmarried','Married')
                combo_married_status.current(0)
                combo_married_status.place(x=560,y=305,width=198,height=22)

        ##--------------------------------------------Date Of Joining---------------------------------------------------##
                label_date_of_joining=Label(Upper_frame,text='DOJ                       :',font=("arial",11,'bold'),bg='white')
                label_date_of_joining.place(x=410,y=340,width=130,height=22)

                label_date_of_joining=ttk.Entry(Upper_frame,textvariable=self.var_doj,width=25,font=('arial',10,'bold'))
                label_date_of_joining.place(x=560,y=340,width=198,height=22)

        ##----------------------------------------------GENDER----------------------------------------------------------##
                label_gender=Label(Upper_frame,text='Gender        :',font=("arial",11,'bold'),bg='white')
                label_gender.place(x=808,y=230,width=100,height=22)

        # label_gender=ttk.Entry(Upper_frame,width=25,font=('arial',11,'bold'))

                combo_gender=ttk.Combobox(Upper_frame,textvariable=self.var_gender,font=('Arial',10,'bold'),width=25,state='readonly')
                combo_gender['value']=('Select','Male','Female','Transgender')
                combo_gender.current(0)
                combo_gender.place(x=920,y=230,width=198,height=22)

        ##---------------------------------------------Phone-----------------------------------------------------------##
                label_phone=Label(Upper_frame,text='Phone          :',font=("arial",11,'bold'),bg='white')
                label_phone.place(x=808,y=267,width=100,height=22)

                label_phone=ttk.Entry(Upper_frame,textvariable=self.var_phone,width=25,font=('arial',10,'bold'))
                label_phone.place(x=920,y=267,width=198,height=22)

        # ##-------------------------------------------------COUNTRY-----------------------------------------------------##
                label_country=Label(Upper_frame,text='Country        :',font=("arial",11,'bold'),bg='white')
                label_country.place(x=808,y=304,width=100,height=22)

                label_country=ttk.Entry(Upper_frame,textvariable=self.var_country,width=25,font=('arial',10,'bold'))
                label_country.place(x=920,y=304,width=198,height=22)

        ##----------------------------------------------SALARY---------------------------------------------------------##
                label_salary=Label(Upper_frame,text='Salary(CTC) :',font=("arial",11,'bold'),bg='white')
                label_salary.place(x=807,y=340,width=100,height=22)

                label_salary=ttk.Entry(Upper_frame,textvariable=self.var_salary,width=25,font=('arial',10,'bold'))
                label_salary.place(x=920,y=340,width=198,height=22)

        ##------------------------------------------------Button Frame------------------------------------------------##

                button_frame=Frame(Upper_frame,bd=4,relief=RIDGE,bg='white')
                button_frame.place(x=1155,y=220,width=175,height=227)
        ##------------------------------SAVE Button-------------------------------------------------------------------##
                btn_add=Button(button_frame,text='SAVE',command=self.add_data, font=('arial',15,'bold'),width=11,bg='blue',fg='white',activeforeground="black",activebackground="blue")
                btn_add.grid(row=0,column=0,padx=13,pady=8)

        ##-----------------------------------------UPDATE BUTTON------------------------------------------------------##
                btn_update=Button(button_frame,text='UPDATE',command=self.update_data,font=('arial',15,'bold'),width=11,bg='blue',fg='white',activeforeground="black",activebackground="blue")
                btn_update.grid(row=1,column=0,padx=13,pady=5)

        ##-----------------------------------------DELETE BUTTON------------------------------------------------------##
                btn_delete=Button(button_frame,text='DELETE', command=self.delete_data,font=('arial',15,'bold'),width=11,bg='red',fg='white',activeforeground="black",activebackground="blue")
                btn_delete.grid(row=2,column=0,padx=13,pady=6)

        ##-------------------------------------------RESET BUTTON------------------------------------------------------##
                btn_clear=Button(button_frame,text='RESET',command=self.rest_data, font=('arial',15,'bold'),width=11,bg='blue',fg='white',activeforeground="black",activebackground="blue")
                btn_clear.grid(row=3,column=0,padx=13,pady=5)


        ##------------------------------Down Frame in Main Frame------------------------------------------------------##
                Down_frame =LabelFrame(Main_frame,bd=4,relief=RIDGE, bg="white",text="Employee Information Table ",font=('times new roman',15,'bold'),fg='red').place(x=25,y=453,width=1315,height=234)

        ##------------------------------------------Search Frame------------------------------------------------------##
                search_frame=LabelFrame(Down_frame,bd=4,relief=RIDGE,text='Search Employee Information',font=('times new roman',12,'bold'),bg='white',fg='#dc3545')
                search_frame.place(x=40,y=474,width=1285,height=65)

        ##-----------------------------------------Search Bar---------------------------------------------------------##
                
                search_by=Label(search_frame,text='Search By :',font=('arial',11,'bold'),bg='white',fg='red',activebackground='white',activeforeground='red')
                search_by.grid(row=0,column=0,padx=5,pady=3)

                self.var_com_search=StringVar()
                combo_search=ttk.Combobox(search_frame, textvariable=self.var_com_search,state='readonly',font=('arial',10,'bold'),width=20)
                combo_search['value']=('Select Option','phone','Idproof')
                combo_search.current(0)
                combo_search.grid(row=0,column=1,padx=10,pady=5)

                self.var_search=StringVar()
                txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=('arial',11,'bold'))
                txt_search.grid(row=0,column=2)

        ##-----------------------------------------Search Button------------------------------------------------------##
                btn_search=Button(search_frame,text="Search",command=self.search_data,  font=('arial',12,'bold',),width=18,bg='blue',fg='white',activebackground='blue',activeforeground='black')
                btn_search.grid(row=0,column=3,padx=30,pady=0)

                btn_showAll=Button(search_frame,text="Show All",command=self.fetch_data,font=('arial',12,'bold',),width=18,bg='blue',fg='white',activebackground='blue',activeforeground='black')
                btn_showAll.grid(row=0,column=4,padx=0,pady=0)

        ##---------------------------------------------Table Frame----------------------------------------------------##

                table_frame=Frame(Down_frame,bd=4,relief=RIDGE)
                table_frame.place(x=40,y=538,width=1285,height=142)

        ##------------------------------------Scroll Bar-------------------------------------------------------------##
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.employee_table=ttk.Treeview(table_frame,column=('dep','name','desigination','email','address','married','dob','doj','Idproof','Id_no.','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.employee_table.xview)
                scroll_y.config(command=self.employee_table.yview)

                self.employee_table.heading('dep',text='DEPARTMENT')
                self.employee_table.heading('name',text='NAME')
                self.employee_table.heading('desigination',text='DESIGINATION')
                self.employee_table.heading('email',text='EMAIL-ID')
                # self.employee_table.heading('password', text="Password")
                self.employee_table.heading('address',text='ADDRESS')
                self.employee_table.heading('married',text='MARRIED STATUS')
                self.employee_table.heading('dob',text='DOB')
                self.employee_table.heading('doj',text='DOJ')
                self.employee_table.heading('Idproof',text='ID PROOF')
                self.employee_table.heading('Id_no.',text='ENTER ID NO.')
                self.employee_table.heading('gender',text='GENDER')
                self.employee_table.heading('phone',text='PHONE')
                self.employee_table.heading('country',text='COUNTRY')
                self.employee_table.heading('salary',text='SALARY')
                
        ##------------------------------SHOW HEADING ON TABLE FRAME--------------------------------------------------##
                self.employee_table['show']='headings'

                self.employee_table.column('dep',width=120)
                self.employee_table.column('name',width=120)
                self.employee_table.column('desigination',width=120)
                self.employee_table.column('email',width=120)
                # self.employee_table.column('password',width=120)
                self.employee_table.column('address',width=120)
                self.employee_table.column('married',width=120)
                self.employee_table.column('dob',width=120)
                self.employee_table.column('doj',width=120)
                self.employee_table.column('Idproof',width=120)
                self.employee_table.column('Id_no.',width=120)
                self.employee_table.column('gender',width=120)
                self.employee_table.column('phone',width=120)
                self.employee_table.column('country',width=120)
                self.employee_table.column('salary',width=120)

                self.employee_table.pack(fill=BOTH,expand=1)


##------------------------------------------Table se Data ko Bind Krne Ke liye----------------------------------------##
                self.employee_table.bind('<ButtonRelease>', self.get_cursor)


##--------------------------------------------Table se Data fetch krne hetu------------------------------------------##
                self.fetch_data()


##-------------------------------------Function--Decelarations--------------------------------------------------------##

        def add_data(self):
                if self.var_dep.get()=='' or self.var_email.get()=='' :
                        messagebox.showerror('Error','All Fields are required')
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",username="root",password='admin',database='company')
                                my_cursor=conn.cursor()
                                my_cursor.execute('Insert into employee value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                        self.var_dep.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_desigination.get(),
                                                                                        self.var_email.get(),
                                                                                        # self.var_password.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_married.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_doj.get(),
                                                                                        self.var_Idproof.get(),
                                                                                        self.var_Id_no.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_country.get(),
                                                                                        self.var_salary.get(),
                                                                                                           ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Successful",'Employee has been Added',parent=self.root)
                        except Exception as es:
                                messagebox.showerror('Error',f'Due To : {str(es)}',parent=self.root)

##---------------------------------------------Fetch Data------------------------------------------------------------##
        def fetch_data(self):
                conn=mysql.connector.connect(host='localhost',username='root',password='admin',database='company')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee')
                data=my_cursor.fetchall()
                if len(data)!=0:
                        self.employee_table.delete(*self.employee_table.get_children())
                        for i in data:
                                self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()

        def get_cursor(self,event=''):
                Cursor_row=self.employee_table.focus()
                content=self.employee_table.item(Cursor_row)
                data=content['values']

                self.var_dep.set(data[0])
                self.var_name.set(data[1])
                self.var_desigination.set(data[2])
                self.var_email.set(data[3])
                self.var_address.set(data[4])
                self.var_married.set(data[5])
                self.var_dob.set(data[6])
                self.var_doj.set(data[7])
                self.var_Idproof.set(data[8])
                self.var_Id_no.set(data[9])
                self.var_gender.set(data[10])
                self.var_phone.set(data[11])
                self.var_country.set(data[12])
                self.var_salary.set(data[13])
                # self.var_password.set(data[14])


##---------------------------------------------For Update--Button----------------------------------------------------##
        def update_data(self):
                if self.var_dep.get()=="" or self.var_email.get()=="":
                        messagebox.showerror('Error','All Feilds are Required')
                else:
                        try:
                                update=messagebox.askyesnocancel('Update','Are You Sure Update this Employee Data')
                                if update >0:
                                        conn=mysql.connector.connect(host='localhost',username='root',password='admin',database='company')
                                        my_cursor=conn.cursor()
                                        my_cursor.execute('update employee set Department =%s,Name=%s,Desigination=%s,Email=%s,Address=%s,Married=%s,DOB=%s,DOJ=%s,Id_no=%s,Gender=%s,phone=%s,Country=%s,Salary=%s where Idproof=%s',(

                                                                                        self.var_dep.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_desigination.get(),
                                                                                        self.var_email.get(),
                                                                                        # self.var_password.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_married.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_doj.get(),
                                                                                        self.var_Idproof.get(),
                                                                                        self.var_Id_no.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_country.get(),
                                                                                        self.var_salary.get(),
                                                                                        

                                                                                                                ))
                                else:
                                        if not update:
                                                return
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo('Success','Employee Successfully Updated',parent=self.root)
                        except Exception as es:
                                messagebox.showerror('Error',f'Due To: {str(es)}',parent=self.root)

##--------------------------------------------Delete Function Button------------------------------------------##       
        def delete_data(self):
                if self.var_Idproof.get()=="" or self.var_email.get()=="" :
                        messagebox.showerror('Error','All Field are required')
                else:
                        try :
                                Delete=messagebox.askyesnocancel('Delete','Are You sure delete this Employee',parent=self.root)
                                if Delete>0:
                                        conn=mysql.connector.connect(host='localhost',username='root',password='admin',database='company')
                                        my_cursor=conn.cursor()
                                        sql='delete from Employee where Idproof=%s'
                                        Value=(self.var_Idproof.get(),)
                                        my_cursor.execute(sql,Value)
                                else:
                                        if not Delete:
                                             return
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo('Delete','Employee Successfully Deleted',parent=self.root)
                        except Exception as es:
                                messagebox.showerror('Error',f'Due To: {str(es)}',parent=self.root)

##-----------------------------------------RESET BUTTON------------------------------------------------------------##

        def rest_data(self):

                self.var_dep.set("Select Department")
                self.var_name.set("")
                self.var_desigination.set("")
                self.var_email.set("")
                # self.var_password.set("")
                self.var_address.set("")
                self.var_married.set("Select")
                self.var_dob.set("")
                self.var_doj.set("")
                self.var_Idproof.set("Select ID Proof")
                self.var_Id_no.set("")
                self.var_gender.set("Gender")
                self.var_phone.set("")
                self.var_country.set("")
                self.var_salary.set("")



##----------------------------------------SEARCH BUTTON--------------------------------------------------------------##
        def search_data(self):
                if self.var_com_search.get()=='' or self.var_search.get()=='' :
                        messagebox.showerror('Error','Please Select Option')
                else:
                        try:
                                conn=mysql.connector.connect(host='localhost',username='root',password='admin',database='company')
                                my_cursor=conn.cursor()
                                my_cursor.execute('Select * from employee where' +str(self.var_com_search.get())+ " 'LIKE' % "+str(self.var_search.get()+"% "))
                                rows=my_cursor.fetchall()

                                if len(rows)!=0:
                                        self.employee_table.delete(*self.employee_table.get_children())
                                        for i in rows:
                                                self.employee_table.insert("",END,values=i)
                                        conn.commit()
                                        self.fetch_data()
                                        conn.close()
                        except Exception as es:
                                messagebox.showerror('Error', f'Due To:{str(es)}',parent=self.root)


                

if __name__ =="__main__":

    root=Tk()
    obj= Employe(root)
    root.mainloop()        
        

