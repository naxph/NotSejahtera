# ********************************************************* 
# Program: YOUR_FILENAME.py 
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN 
# Class: TT0? 
# Trimester: 2110
# Year: 2021/22 Trimester 1 
# Member_1: 1211101734 | ERNEST LEONG ZHENG YANG | 1211101734@student.mmu.edu.my | 01155355639
# Member_2: 1211101591 | IAN LEONG TSUNG JII | 211101591@student.mmu.edu.my | 0192835699
# Member_3: 1211101790 | LEE HENG YEP | 1211101790@student.mmu.edu.my | 0188703882
# Member_4: ID | NAME | EMAIL | PHONES 
# *********************************************************
# Task Distribution
# Member_1: Menu and result display
# Member_2: Account sign up and login authentication
# Member_3: Administrator assign appointment, create vaccination centre and generate list
# Member_4:
# *********************************************************




from tkinter import*
from tkinter import messagebox

#frame1
def showframe1():
    exit()

#Switch frames
def show_frame(frame):
    frame.tkraise()

#User sign up
def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open("user_details.txt","r")
    for i in file.readlines():
        a,b = i.split(",")
        a = a.strip()
        b = b.strip()
        if len(username.get() and password.get()) == 0:
           error = messagebox.showerror("Cool Beans", "fields cannot be empty, idiot")
           Label(frame2, text=error)
           break
        elif len(username.get() and password.get()) < 5:
           error1 = messagebox.showerror("Cool Beans", "Username and password must have at least 6 characters")
           Label(frame2, text=error1)
           break
        elif "," in username.get() or "," in password.get():
           error2 = messagebox.showerror("Cool Beans", "Username and password cannot contain ',' ")
           Label(frame2, text=error2)
           break
        elif(a == username.get()):
           error3 = messagebox.showerror("Cool Beans", "Username already taken ")
           Label(frame2, text=error3)
           break
    else:
        file = open("user_details.txt","a")
        file.write("\n"+username_info+","+password_info)
        file.close()
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        info = messagebox.showinfo("Cool Beans", "Registration successful")
        Label(frame2, text = info)

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
            login_success1()
            break
    else:
        wrong_password1()

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
            current_username(username1)
            login_success()
            global infoscreen
            infoscreen = 0
            break
    else:
        wrong_password()

#public user
def login_success():
    messagebox.showinfo("Cool Beans", "Login Successful")
    show_frame(frame5)
    #public user main page goes here

def wrong_password():
    messagebox.showinfo("Cool Beans", "wrong username or password")
    show_frame(frame1)

#admin
def login_success1():
    messagebox.showinfo("Cool Beans", "Login successful. Welcome Admin")
    show_frame(frame10)
    #admin main page goes here
    
def wrong_password1():
    messagebox.showinfo("Cool Beans", "wrong username or password")
    show_frame(frame1)

#personal information update system
def no_password(): #shows error if wrong username or password
    messagebox.showinfo("Error", "Wrong username or password")
    show_frame(frame5)


def already_registered(): #shows error if the user has already registered
    messagebox.showinfo("Error", "You have already registered for vaccination. Please check the Vaccination Appointment Status page within 3-5 days for updates.")
    usernameUpdateEntry.delete(0,END)
    passwordUpdateEntry.delete(0,END)
    fullNameEntry.delete(0,END)
    ageEntry.delete(0,END)
    phoneEntry.delete(0,END)
    postcodeEntry .delete(0,END)
    occupationEntry.delete(0,END)  
    show_frame(frame5)


def check_register(): #checks if user has registered for vaccine
    username1 = usernameUpdateEntry.get()
    password1 = passwordUpdateEntry.get()
    readFile = open("user_personalinfo.txt", "r")

    for line in readFile:
        a,b,c,d,e,f,g,h = line.split(",")
        a = a.strip()
        b = b.strip()
        c = c.strip()
        d = d.strip()
        e = e.strip()
        f = f.strip()
        g = g.strip()
        h = h.strip()

        if(a == username1 and b == password1):
            already_registered()
            break
    else:
        update_success()
        

def update_success(): #writes information to file
    username1 = usernameUpdateEntry.get()
    password1 = passwordUpdateEntry.get()
    fullNameInfo = fullNameEntry.get()
    ageInfo = ageEntry.get()
    phoneInfo = phoneEntry.get()
    postcodeInfo = postcodeEntry.get()
    occupationInfo = occupationEntry.get()
    chronicDiseaseInfo = chronicDisease.get()
    updateFile = open("user_personalinfo.txt", "a")

    if chronicDiseaseInfo == 1:
        updateFile.write("\n"+username1+","+password1+","+fullNameInfo+","+ageInfo+","+phoneInfo+","+postcodeInfo+","+occupationInfo+","+"True")
        updateFile.close()
    elif chronicDiseaseInfo == 0:
        updateFile.write("\n"+username1+","+password1+","+fullNameInfo+","+ageInfo+","+phoneInfo+","+postcodeInfo+","+occupationInfo+","+"False")
        updateFile.close()

    usernameUpdateEntry.delete(0,END)
    passwordUpdateEntry.delete(0,END)
    fullNameEntry.delete(0,END)
    ageEntry.delete(0,END)
    phoneEntry.delete(0,END)
    postcodeEntry.delete(0,END) 
    occupationEntry.delete(0,END)   
    messagebox.showinfo("Registration Successful", "Your registration for the COVID-19 Vaccine was successful. Please check the Vaccination Appointment Status page within 3-5 days for updates.")
    show_frame(frame5)
    

def update_info(): #checks if username and password are correct
    username1 = usernameUpdateEntry.get()
    password1 = passwordUpdateEntry.get()
    readFile = open("user_details.txt", "r")
    
    for line in readFile:
        a,b = line.split(",")
        a = a.strip()
        b = b.strip()
        if(a == username1 and b == password1):
            check_register()
            break
    else:
        no_password()

tempuser = None
def current_username(a): #Checks current username
    global tempuser
    tempuser = "none"
    tempuser = a
    info_screen()


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
frame8 = Frame(screen) #add/remove vaccination centre
frame9 = Frame(screen) #assign user
frame10 = Frame(screen) #admin menu
screen.rowconfigure(0, weight=1)
screen.columnconfigure(0, weight=1)
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
password_entry1 = Entry(frame3,textvariable=password_verify,show="*") #changed to * characters
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
password_entry2 = Entry(frame4,textvariable=password_verify1, show="*")
password_entry2.pack()
Label(frame4,text = "").pack()
Button(frame4, text = "Login",width = 10, height=1,command = admin_verify).pack()
Label(frame4,text = "").pack()
Button(frame4, text = "Back",width = 10, height=1,command = lambda:show_frame(frame1)).pack()


#information screen after login
infoscreen = 1
risk_status = ''
occupation_status = ''
def info_screen():
    openAnother = open("user_personalinfo.txt","r")
    xdlines = list(openAnother.readlines())
    global infoscreen

    if infoscreen  == 1:
        for i in xdlines:
            a, b, c, d, e, f, g, h = i.split(",")
            a = a.strip()
            b = b.strip()
            c = c.strip()
            d = d.strip()
            e = e.strip()
            f = f.strip()
            g = g.strip()
            h = h.strip()
            if a == tempuser:
                global occupation_status
                occupation_status = h
                if (int(d) > 60) or (g =="True"):
                    global risk_status
                    risk_status = "High"

                else:
                    risk_status = "Low"

        Label(frame5,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
        Label(frame5,text = f"Welcome back, {tempuser}. Your current risk status is {risk_status}.", font = ("Calibri", 20), pady = 50, padx = 10).pack()
        Button(frame5, text = "Vaccine Registration",width = 50, height=1, pady = 20, command = lambda:show_frame(frame6)).pack()
        Button(frame5, text = "Vaccination Appointment Status",width = 50, height=1, pady = 20, command = appointment_status).pack()
        Button(frame5, text = "Logout",width = 50, height=1, pady = 20, command = showframe1).pack()


#vaccination registration form
Label(frame6,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame6,text = "Please enter your personal details to register yourself for a vaccine appointment. Please ensure your personal details are correct before submitting.", pady = 20, padx = 20, font = ("Calibri", 10)).pack()
Label(frame6,text = "Current Username", pady = 10).pack()
usernameUpdateEntry = Entry(frame6, width=15)
usernameUpdateEntry.pack()
Label(frame6,text = "Current Password", pady = 10).pack()
passwordUpdateEntry = Entry(frame6, width=15, show="*")
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
Label(frame6,text = "Occupation", pady = 5).pack()
occupationEntry = Entry(frame6, width=20)
occupationEntry.pack()
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
tempdate = ""
templocation = ""
temptime = ""

def appointment_status():
    readVaccination = open("vaccination.txt","r")
    xdlines = list(readVaccination.readlines())

    for i in xdlines:
        a, b, c, d, e, f, g, h, j = i.split(",")
        a = a.strip() #name
        b = b.strip() #age
        c = c.strip() #occupation
        d = d.strip() #username
        e = e.strip() #risk status
        f = f.strip() #location
        g = g.strip() #point
        h = h.strip() #time
        j = j.strip() #date
        if tempuser == d:
            global templocation
            templocation =  g + ',' + f
            global temptime
            temptime = h
            global tempdate
            tempdate = j
            readVaccination.close()
            break
        
    show_frame(frame7)
    Label(frame7,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
    Label(frame7, text=f"Appointment Date: \n {tempdate}", pady = 20).pack()
    Label(frame7, text=f"Appointment Time: \n {temptime}", pady = 40).pack()
    Label(frame7, text=f"Appointment Location: \n {templocation}", pady = 50).pack()
    Label(frame7,text = "Are you going to attend the appointment?", pady = 10).pack()
    Appointment = IntVar()
    yesButton = Radiobutton(frame7, text="Yes", variable=Appointment, value=1, command = yesAttend)
    yesButton.pack()
    noButton = Radiobutton(frame7, text="No", variable=Appointment, value=0, command = noAttend)
    noButton.pack()
    Button(frame7, text = "Back",width = 50, height=1, pady = 10, command = lambda:show_frame(frame5)).pack()
    
def yesAttend():
    x = open ('vaccination_RSVP.txt', 'a')
    x.write(f'RSVP : {tempuser}, Yes\n')
    x.close()

def noAttend():
    x = open ('vaccination_RSVP.txt', 'a')
    x.write(f'RSVP : {tempuser}, No\n')
    x.close()




#add/remove vaccination centre

Vac_centre=['Cyberjaya, MMU, 8.00 am, 19/11/2021','Serdang, Hospital Serdang, 8.00am, 20/11/2021','Subang Jaya, INTI University, 8.00am, 21/11/2021']


def add():
    x = textbox.get()
    vac_list.insert((len(Vac_centre)+1),x)
    textbox.delete(0,END)
    Vac_centre.append(x)
    return

# deletes selected item
def remove():
    y = vac_list.curselection()
    for i in y[::-1]:
        vac_list.delete(i)
        return


var1 = StringVar()

vac_list = Listbox(frame8,height=20,width=50,selectmode=EXTENDED,listvariable=var1)
for i in range(len(Vac_centre)):
    vac_list.insert(i,(Vac_centre[i]))

# scrollbar
vac_listS = Scrollbar(frame8)
vac_listS.pack(side=RIGHT,fill=Y)
vac_list.config(yscrollcommand=vac_listS.set)
vac_listS.config(command=vac_list.yview)


add_button = Button(frame8,text='Add vaccination centre',command=lambda: add())
remove_button = Button(frame8,text='Remove vaccination centre',command=lambda: remove())
textbox = Entry(frame8,text = '',width=50)
space = Label(frame8, text='', pady=50)
space2 = Label(frame8,text='')


space.pack()
vac_list.pack()
textbox.pack()
space2.pack()
add_button.pack()
remove_button.pack()
space2.pack()
Button(frame8,text='Back',command=lambda:show_frame(frame10)).pack()

# assign shit

def assign_user():
    openVaccination = open("vaccination.txt","a")
    x = user_list.get(user_list.curselection()) +', '+ vac_list2.get(vac_list2.curselection())
    assigned_user.insert(END,x)
    openVaccination.write(x + '\n')
    openVaccination.close()

lines2 = []
def remove_user():
    assigned_user.delete(END,assigned_user.curselection())
    with open (r'vaccination.txt', 'r') as fileread:
        linesread = fileread.readlines()

    with open (r'vaccination.txt', 'w') as fileread:

        for i in (linesread):
            a, b, c, d, e, f, g, h = i.strip('\n')
            a = a.strip() # user name
            b = b.strip()
            c = c.strip()
            d = d.strip()
            e = e.strip()
            f = f.strip()
            g = g.strip()
            h = h.strip()
            if a in assigned_user.curselection():
                fileread.write(line)



    
user_list=Listbox(frame9,height=30,width=60,exportselection=0)
vac_list2 = Listbox(frame9,height=30,width=60,exportselection=0,listvariable=var1)
assigned_user=Listbox(frame9,height=30,width=60)

# scrollbar
user_listS = Scrollbar(frame9)
user_listS.grid(row=1,column=2,rowspan=5)
user_list.config(yscrollcommand=user_listS.set)
user_listS.config(command=user_list.yview)

vac_list2S = Scrollbar(frame9)
vac_list2S.grid(row=1,column=4,rowspan=5)
vac_list2.config(yscrollcommand=vac_list2S.set)
vac_list2S.config(command=vac_list2.yview)

assigned_userS = Scrollbar(frame9)
assigned_userS.grid(row=1,column=6,rowspan=5)
assigned_user.config(yscrollcommand=assigned_userS.set)
assigned_userS.config(command=assigned_user.yview)


user_details = list(open('user_personalinfo.txt').readlines())
for line in user_details:
    a,b,c,d,e,f,g,h = line.split(",")
    a = a.strip() #username
    b = b.strip() #password
    c = c.strip() #full name
    d = d.strip() #age
    e = e.strip() #phone number
    f = f.strip() #postcode
    g = g.strip().lower() #occupation
    h = h.strip() #chronic disease status

    if g =='doctor'or g =='nurse' or g=='soldier' :
        risk_level = 5
    elif g=='teacher' or g=='lecturer' or g =='student' or g=='politician':
        risk_level = 4
    elif g=='motorsport driver' or g=='chef':
        risk_level = 3
    elif g=='ship technician':
        risk_level = 2
    elif g=='unemployed' or g=='youtuber' or g=='software engineer':
        risk_level = 1
    else:
        risk_level = 'cyak blyt'
    user_list.insert(END,f'{c}, {d}, {g}, {a}, {risk_level}')


assign_button= Button(frame9,text='Assign',command=assign_user)
removeuser_button= Button(frame9,text='Remove',command=remove_user)


# empty space
Label(frame9,text='').grid(row=0)
Label(frame9,text='').grid(row=1,column=0,padx=90)
# not empty space
Button(frame9,text='Back',command=lambda:show_frame(frame10)).grid(row=5,column=3)
user_list.grid(row=1,column=1,padx=10,pady=10)
vac_list2.grid(row=1,column=3,padx=10,pady=10)
assigned_user.grid(row=1,column=5,padx=10,pady=10)
assign_button.grid(row=2,column=3)
removeuser_button.grid(row=3,column=3)


#admin menu
Label(frame10,text = "NotSejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame10,text='Welcome Admin.',pady=30).pack()
Label(frame10,text='',height=15).pack()
Button(frame10, text = "Edit vaccination centre",width=20,height=1,command = lambda:show_frame(frame8)).pack()
Label(frame10,text='').pack()
Button(frame10, text = "Assign user",width=20,height=1,command = lambda:show_frame(frame9)).pack()
Label(frame10,text='').pack()
Button(frame10,text='Back',width=20,height=1,command=lambda:show_frame(frame1)).pack()


screen.mainloop()
