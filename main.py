from tkinter import*
from tkinter import messagebox

def show_frame(frame):
    frame.tkraise()

def register_user():
    username_info = username.get()
    password_info = password.get()
    if len(username.get() and password.get()) == 0:
        error = messagebox.showerror("Cool Shit", "fields cannot be empty, idiot")
        Label(frame2, text=error)
    else:
       file=open("user_details.txt","a")
       file.write("\n"+username_info+","+password_info)
       file.close()
       username_entry.delete(0,END)
       password_entry.delete(0,END)
       Label(frame2, text = "Registration successful",fg="green",font=("Calibri", 12)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
    
    file=open("user_details.txt","r")
    for i in file:
        a,b = i.split(",")
        a = a.strip()
        b = b.strip()
        if(a == username1 or b == password1):
            login_success()
            break
        else:
            wrong_password()
            break
                

def login_success():
    response = messagebox.showinfo("Cool Shit", "Login successful")
    Label(frame3,text = response).pack()
    show_frame(frame4)
    
def wrong_password():
    response1 = messagebox.showinfo("Cool Shit", "wrong username or password")
    Label(frame3, text = response1).pack()
    show_frame(frame1)

#startup screen
global screen
screen = Tk()
screen.state("zoomed")
screen.title("MySejahtera")
frame1 = Frame(screen)
frame2 = Frame(screen)
frame3 = Frame(screen)
frame4 = Frame(screen)
screen.rowconfigure(0, weight=1)
screen.columnconfigure(0,weight=1)
for frame in(frame1,frame2,frame3,frame4):
    frame.grid(row=0,column=0,sticky="nsew")
show_frame(frame1)
Label(frame1,text = "MySejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame1,text = "",height=18).pack()
Button(frame1,text = "login", height = "2", width = "30", command = lambda:show_frame(frame3)).pack()
Label(frame1,text = "").pack()
Button(frame1,text = "register", height = "2", width = "30", command=lambda:show_frame(frame2)).pack()


#register
global username
global password
global username_entry
global password_entry
username = StringVar()
password = StringVar()
Label(frame2,text = "MySejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
Label(frame2,text = "Username * ").pack()
username_entry = Entry(frame2,textvariable=username)
username_entry.pack()
Label(frame2,text = "Password * ").pack()
password_entry = Entry(frame2,textvariable=password)
password_entry.pack()
Label(frame2,text = "").pack()
Button(frame2,text="Register",width = 10, height = 1,command = register_user).pack()
Label(frame2,text = "").pack()
Button(frame2,text="back",width = 10, height = 1,command =lambda:show_frame(frame1)).pack()

#login
Label(frame3,text = "MySejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')
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

#main
Label(frame4,text = "MySejahtera",bg = "grey", font = ("Calibri", 20)).pack(fil = 'x')




screen.mainloop()