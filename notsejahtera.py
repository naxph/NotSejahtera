from tkinter import*
from tkinter import messagebox

#Switch frames
def show_frame(frame):
    frame.tkraise()

#User sign up
def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open("user_details.txt","r")
    for i in file:
        a,b = i.split(",")
        a = a.strip()
        b = b.strip()
    if len(username.get() and password.get()) == 0:
        error = messagebox.showerror("Cool Beans", "fields cannot be empty, idiot")
        Label(frame2, text=error)
    elif len(username.get() and password.get()) < 5:
        error1 = messagebox.showerror("Cool Beans", "Username and password must have at least 6 characters")
        Label(frame2, text=error1)
    elif "," in username.get() or "," in password.get():
       error2 = messagebox.showerror("Cool Beans", "Username and password cannot contain ',' ")
       Label(frame2, text=error2)
    elif(a == username_info):
       error3 = messagebox.showerror("Cool Beans", "Username already taken ")
       Label(frame2, text=error3)
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

#information update system
def no_password():
    messagebox.showinfo("Error", "Wrong username or password")
    show_frame(frame5)


def update_success():
    username1 = usernameUpdateEntry.get()
    password1 = passwordUpdateEntry.get()
    fullNameInfo = fullNameEntry.get()
    ageInfo = ageEntry.get()
    phoneInfo = phoneEntry.get()
    postcodeInfo = postcodeEntry.get()
    chronicDiseaseInfo = chronicDisease.get()
    updateFile = open("user_personalinfo.txt", "a")

    if chronicDiseaseInfo == 1:
        updateFile.write("\n"+username1+","+password1+","+fullNameInfo+","+ageInfo+","+phoneInfo+","+postcodeInfo+","+"True")
        updateFile.close()
    elif chronicDiseaseInfo == 0:
        updateFile.write("\n"+username1+","+password1+","+fullNameInfo+","+ageInfo+","+phoneInfo+","+postcodeInfo+","+"False")
        updateFile.close()

    usernameUpdateEntry.delete(0,END)
    passwordUpdateEntry.delete(0,END)
    fullNameEntry.delete(0,END)
    ageEntry.delete(0,END)
    phoneEntry.delete(0,END)
    postcodeEntry .delete(0,END)    
    messagebox.showinfo("Registration Successful", "Your registration for the COVID-19 Vaccine was successful. Please check the Vaccination Appointment Status page within 3-5 days for updates.")
    show_frame(frame5)
    

def update_info():
    username1 = usernameUpdateEntry.get()
    password1 = passwordUpdateEntry.get()
    readFile = open("user_details.txt", "r")
    
    for line in readFile:
        a,b = line.split(",")
        a = a.strip()
        b = b.strip()
        if(a == username1 and b == password1):
            update_success()
            break
    else:
        no_password()


#startup screen
global screen
screen = Tk()
screen.state("zoomed")
screen.title("NotSejahtera")
frame1 = Frame(screen) #startup screen
frame2 = Frame(screen) #register screen
frame3 = Frame(screen) #public user login screen
frame4 = Frame(screen) #admin login screen
frame5 = Frame(screen) #public user main landing page for after login
frame6 = Frame(screen) #public user vaccination registration form
frame7 = Frame(screen) #public user vaccination appointment status page
frame8 = Frame(screen) #unused
frame9 = Frame(screen) #unused
frame10 = Frame(screen) #unused
screen.rowconfigure(0, weight=1)
screen.columnconfigure(0,weight=1)
for frame in(frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9,frame10):
    frame.grid(row=0,column=0,sticky="nsew")

show_frame(frame1)
Label(frame1,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame1,text = "",height=18).pack()
Button(frame1,text = "Login", height = "2", width = "30", command = lambda:show_frame(frame3)).pack()
Label(frame1,text = "").pack()
Button(frame1,text = "Register", height = "2", width = "30", command= lambda:show_frame(frame2)).pack()
Label(frame1,text = "").pack()
Button(frame1, text = "Admin Login",height = "2", width = "30", command = lambda:show_frame(frame4)).pack()
Label(frame1,text = "").pack()


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
Button(frame5, text = "Vaccine Registration",width = 50, height=1, pady = 20, command = lambda:show_frame(frame6)).pack()
Button(frame5, text = "Vaccination Appointment Status",width = 50, height=1, pady = 20, command = lambda:show_frame(frame7)).pack()
Button(frame5, text = "Logout",width = 50, height=1, pady = 20, command = lambda:show_frame(frame1)).pack()


#vaccination registration form
Label(frame6,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame6,text = "Please enter your personal details to register yourself for a vaccine appointment. Please ensure your personal details are correct before submitting.", pady = 20, padx = 20, font = ("Calibri", 10)).pack()
Label(frame6,text = "Current Username", pady = 10).pack()
usernameUpdateEntry = Entry(frame6, width=15)
usernameUpdateEntry.pack()
Label(frame6,text = "Current Password", pady = 10).pack()
passwordUpdateEntry = Entry(frame6, width=15)
passwordUpdateEntry.pack()
Label(frame6,text = "Full Name as per NRIC", pady = 10).pack()
fullNameEntry = Entry(frame6, width=70)
fullNameEntry.pack()
Label(frame6,text = "Age", pady = 5).pack() 
ageEntry = Entry(frame6, width=10)
ageEntry.pack()
Label(frame6,text = "Phone Number", pady = 10).pack()
phoneEntry = Entry(frame6, width=20)
phoneEntry.pack()
Label(frame6,text = "Postcode", pady = 5).pack()
postcodeEntry = Entry(frame6, width=20)
postcodeEntry.pack()
Label(frame6,text = "Do you have any chronic illnesses?(Diabetes, heart conditions, etc.)", pady = 10).pack()
chronicDisease = IntVar()
yesButton = Radiobutton(frame6, text="Yes", variable=chronicDisease, value=1)
yesButton.pack()
noButton = Radiobutton(frame6, text="No", variable=chronicDisease, value=0)
noButton.pack()
Label(frame6,text = "").pack()
Label(frame6,text = "").pack()
Button(frame6, text = "Confirm Details",width = 50, height=1, pady = 10, command=update_info).pack()
Button(frame6, text = "Cancel",width = 50, height=1, pady = 10, command = lambda:show_frame(frame5)).pack()
Label(frame6,text = "").pack()

#vaccination appointment status screen
Label(frame7,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Button(frame7, text = "Back",width = 50, height=1, pady = 10, command = lambda:show_frame(frame5)).pack()
#to be continued


screen.mainloop()
