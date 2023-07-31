from tkinter import *
from tkinter import ttk #themed tkinter
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()
    

    if accepted == "Accepted":
        #user_info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
        
            #course info
            registration_status = reg_status_var.get()
            #note that of the check box seem different
            numcourses = numcourses_spinbox.get()
            numsemesters= numsemesters_spinbox.get()

            #line_seperator
            line_seperator = "-------------------------------------------------"

            #print(f"Your Title is : {title}Your FirstName is : {firstname} and Your LastName is : {lastname}")
            print(f"Your Full Name is :  {title} {lastname} {firstname}")
            print(f"You are: {age}years old and Your are from : {nationality}")
            print(f"Total Number of Courses: {numcourses}")
            print(f"Total Number of Semesters: {numsemesters}")
            print(f"{ registration_status}")
            print(f"{line_seperator}")
        else:
             messagebox.showwarning(title = "Error",message = "First Name and Last Name are Required")
    
            

    else:
        messagebox.showwarning(title = "Error",message = "You have not Accepted the Terms")
    
    
    
window = Tk()
window.title("Data Entry Form")
#window.geometry("600x400")

frame = Frame(window)
frame.pack()

#Saving User Info
user_info_frame = LabelFrame(frame,text = "User Information")
user_info_frame.grid(row =0 ,column =0,padx =20,pady = 10)

first_name_label = Label(user_info_frame,text = "First Name")
first_name_label.grid(row =0 ,column =0 )

last_name_label = Label(user_info_frame,text = "Last Name")
last_name_label.grid(row =0 ,column =1)

first_name_entry = Entry(user_info_frame)
first_name_entry.grid(row =1 ,column =0 )

last_name_entry = Entry(user_info_frame)
last_name_entry.grid(row =1 ,column =1 )

title_label = Label(user_info_frame,text = "Title")
title_label.grid(row = 0,column = 2)
title_combobox = ttk.Combobox(user_info_frame,values =["","Mr","Mrs","Dr.","Prof."])
title_combobox.grid(row = 1,column = 2)

age_label = Label(user_info_frame,text = "Age")
age_label.grid(row =2 ,column =0)

age_spinbox = Spinbox(user_info_frame,from_ = 18,to=10000)# = 'infinity'
age_spinbox.grid(row =3 ,column =0)

nationality_label = Label(user_info_frame,text = "Nationality")
nationality_label.grid(row = 2,column = 1)
nationality_combobox = ttk.Combobox(user_info_frame,values =["Africa","Asia","Austrialia","South American","Oceania"])
nationality_combobox.grid(row = 3,column = 1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 10,pady = 5)

#Saving Course Info
courses_frame = LabelFrame(frame)
courses_frame.grid(row = 1,column = 0,sticky = "news",padx =20,pady=10)

registered_label = Label(courses_frame,text = "Registration Status")
registered_label.grid(row =0 ,column =0)

reg_status_var = StringVar(value = "Not Registered")
registered_check = Checkbutton(courses_frame
                               ,text = "Currently Registration"
                               ,variable =reg_status_var,onvalue = "Registered",offvalue="Not Registered")
registered_check.grid(row =1 ,column =0)

numcourses_label = Label(courses_frame,text = "# Completed Courses")
numcourses_label.grid(row =0 ,column =1)

numcourses_spinbox = Spinbox(courses_frame,from_ = 0,to='infinity')
numcourses_spinbox.grid(row =1 ,column =1)

numsemesters_label = Label(courses_frame,text = "# Semesters")
numsemesters_label.grid(row =0 ,column =2)

numsemesters_spinbox = Spinbox(courses_frame,from_ = 0,to='infinity')
numsemesters_spinbox.grid(row =1 ,column =2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx = 10,pady = 5)

#Accept terms
accept_var = StringVar(value = "Not Accepted")
terms_frame = LabelFrame(frame,text = "Terms & Conditions")
terms_frame.grid(row = 2,column = 0,sticky = "news",padx =20,pady=10)

terms_check = Checkbutton(terms_frame
                          ,text = "I accept the terms and Conditions."
                          ,variable = accept_var,onvalue ="Accepted" ,offvalue ="Not Accepted")
terms_check.grid(row =0 ,column =0)

#Button
button = Button(frame,text = "Enter data",command = enter_data)
button.grid(row=3,column = 0,sticky = "news",padx =20,pady=10)


window.mainloop()
