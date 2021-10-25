from tkinter import *
import sys

def com1():
    if entry1.get() == 'admin' and entry2.get() == '123':
        root.deiconify()
        top.destroy()

def com2():
    top.destroy()
    root.destroy()
    sys.exit()


root = Tk()
top = Toplevel()

top.geometry('300x260')
top.title('Pain')
top.configure(background='lightblue')
photo2 = PhotoImage(file='rickroll-roll.gif')
photo = Label(top, image=photo2, background='white')
username = Label(top, text='Username', font=('Arial',10))
entry1 = Entry(top)
password = Label(top, text='Password', font=('Arial',10))
entry2 = Entry(top, show='*')
cancel = Button(top, text='Cancel', command=lambda:com2())

entry2.bind('<Return>',com1)

photo.pack()
username.pack()
entry1.pack()
password.pack()
cancel.pack()

root.title('Insanity')
root.configure(background='white')
root.geometry('855x650')

root.withdraw()
root.mainloop()


#learned from https://www.youtube.com/watch?v=qwBZMUM9L_E
