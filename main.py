from tkinter import*
from tkinter import messagebox

#Switch frames
def show_frame(frame):
    frame.tkraise()

#User sign up
def register_user():
    username_info = username.get()
    password_info = password.get()
    if len(username.get() and password.get()) == 0:
        error = messagebox.showerror("Cool Beans", "fields cannot be empty, idiot")
        Label(frame2, text=error)
    elif len(username.get() and password.get()) < 5:
        error1 = messagebox.showerror("Cool Beans", "Username and password must have at least 6 characters")
        Label(frame2, text=error1)
    elif "," in username.get() or "," in password.get():
       error2 = messagebox.showerror("Cool Beans", "Username and password cannot contain ',' ")
       Label(frame2, text=error2)
    else:
       file=open("user_details.txt","a")
       file.write("\n"+username_info+","+password_info)
       file.close()
       username_entry.delete(0,END)
       password_entry.delete(0,END)
       Label(frame2, text = "Registration successful",fg="green",font=("Calibri", 12)).pack()

#admin login verification
def admin_verify():
    username = username_verify1.get()
    password = password_verify1.get()
    username_entry2.delete(0,END)
    password_entry2.delete(0,END)
    
    file = open("admin_details.txt","r")
    for i in file:
        a,b = i.split(",")
        a = a.strip()
        b = b.strip()
        if(a == username and b == password):
            login_success()
            break
    else:
        wrong_password()

#public user login verification
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
    
    file = open("user_details.txt","r")
    for i in file:
        a,b = i.split(",")
        a = a.strip()
        b = b.strip()
        if(a == username1 and b == password1):
            login_success()
            break
    else:
        wrong_password()
                
#public user
def login_success():
    messagebox.showinfo("Cool Beans", "Login successful")
    show_frame(frame5)
    #public user main page goes here

def wrong_password():
    messagebox.showinfo("Cool Beans", "wrong username or password")
    show_frame(frame1)

#admin
def login_success1():
    messagebox.showinfo("Cool Beans", "Login successful. Welcome Admin")
    show_frame(frame6)
    #admin main page goes here
    
def wrong_password1():
    messagebox.showinfo("Cool Beans", "wrong username or password")
    show_frame(frame1)

#startup screen
global screen
screen = Tk()
screen.state("zoomed")
screen.title("NotSejahtera")
frame1 = Frame(screen)
frame2 = Frame(screen)
frame3 = Frame(screen)
frame4 = Frame(screen)
frame5 = Frame(screen)
frame6 = Frame(screen)
screen.rowconfigure(0, weight=1)
screen.columnconfigure(0,weight=1)
for frame in(frame1,frame2,frame3,frame4,frame5,frame6):
    frame.grid(row=0,column=0,sticky="nsew")

show_frame(frame1)
Label(frame1,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame1,text = "",height=18).pack()
Button(frame1,text = "Login", height = "2", width = "30", command = lambda:show_frame(frame3)).pack()
Label(frame1,text = "").pack()
Button(frame1,text = "Register", height = "2", width = "30", command= lambda:show_frame(frame2)).pack()
Label(frame1,text = "").pack()
Button(frame1, text = "Admin Login",height = "2", width = "30", command = lambda:show_frame(frame4)).pack()


#register
global username
global password
global username_entry
global password_entry
username = StringVar()
password = StringVar()
Label(frame2,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame2,text = "Please enter details below to Register an account").pack()
Label(frame2,text = "Username * ").pack()
username_entry = Entry(frame2,textvariable=username)
username_entry.pack()
Label(frame2,text = "Password * ").pack()
password_entry = Entry(frame2,textvariable=password)
password_entry.pack()
Label(frame2,text = "").pack()
Button(frame2,text="Register",width = 10, height = 1,command = register_user).pack()
Label(frame2,text = "").pack()
Button(frame2,text="Back",width = 10, height = 1,command =lambda:show_frame(frame1)).pack()

#login
Label(frame3,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame3,text = "Please enter details below to login").pack()
global username_verify
global password_verify
global username_entry1
global password_entry1

username_verify = StringVar()
password_verify = StringVar()

Label(frame3,text = "Username * ").pack()
username_entry1 = Entry(frame3,textvariable=username_verify)
username_entry1.pack()
Label(frame3,text = "").pack()
Label(frame3,text = "Password * ").pack()
password_entry1 = Entry(frame3,textvariable=password_verify)
password_entry1.pack()
Label(frame3,text = "").pack()
Button(frame3, text = "Login",width = 10, height=1,command = login_verify).pack()
Label(frame3,text = "").pack()
Button(frame3, text = "Back",width = 10, height=1,command = lambda:show_frame(frame1)).pack()


#admin login
Label(frame4,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame4,text = "Please enter details below to login").pack()
global username_verify1
global password_verify1
global username_entry2
global password_entry2

username_verify1 = StringVar()
password_verify1 = StringVar()

Label(frame4,text = "Username * ").pack()
username_entry2 = Entry(frame4,textvariable=username_verify1)
username_entry2.pack()
Label(frame4,text = "").pack()
Label(frame4,text = "Password * ").pack()
password_entry2 = Entry(frame4,textvariable=password_verify1)
password_entry2.pack()
Label(frame4,text = "").pack()
Button(frame4, text = "Login",width = 10, height=1,command = admin_verify).pack()
Label(frame4,text = "").pack()
Button(frame4, text = "Back",width = 10, height=1,command = lambda:show_frame(frame1)).pack()


#information screen after login
Label(frame5,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame5,text = "Welcome back, <USER>. Your current risk status is <RISK FACTOR>.", font = ("Calibri", 20), pady = 50, padx = 10).pack()
Button(frame5, text = "Click here to update your Personal Information",width = 50, height=1, pady = 20, command = lambda:show_frame(frame6)).pack()
Button(frame5, text = "Vaccination Appointment Status",width = 50, height=1, pady = 20, command = lambda:show_frame()).pack()

# to be continued



screen.mainloop()