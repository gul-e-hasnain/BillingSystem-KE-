from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("LogIn")
window.geometry("450x520+450+30")
window.resizable(0, 0)
window.config(bg = "white")

def exitt():
    exit()

menu = Menu(window)
window.config(menu = menu)

subm1 = Menu(menu, tearoff = 0)
menu.add_cascade(label = "File", menu = subm1)
subm1.add_command(label = "Exit", command = exitt)

loginImage = PhotoImage(file = "KE_logo.png")
pic = Label(window, image = loginImage, bg = "white")
pic.place(x = 130 , y = 50)

lid = StringVar()
pwd = StringVar()

def login():
    loginId = lid.get()
    password = pwd.get()
    if loginId == "admin" and password =="admin":
        window.destroy()
        import register
    elif loginId == "":
        messagebox.showerror('Alert', 'please enter Login Id to proceed')
    elif password == "":
        messagebox.showerror('Alert', 'please enter Password to proceed')
    else:
        messagebox.showerror('Alert', 'invalid login Id or password')

label1 = Label(window, text = "Login ID: ", width = 20, font = ("bold",10), bg = "white")
label1.place(x = 50, y = 255)

entry1 = Entry(window, width = 30, textvar = lid, relief = "solid", bd = 1)
entry1.place(x = 180, y = 255)

label2 = Label(window, text = "Password: ", width = 20, font = ("bold",10), bg = "white")
label2.place(x = 50, y = 315)

entry2 = Entry(window, width = 30, textvar = pwd, show = "*", relief = "solid", bd = 1)
entry2.place(x = 180, y = 315)

btn1 = Button(window, text = "Log In", font = ("bold", 12), fg = "White", bg = "orange", width = 16, relief = "solid", bd = 1, command=login)
btn1.place(x = 180, y = 390)

window.mainloop()