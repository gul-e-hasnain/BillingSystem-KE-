from tkinter import *
window2 = Tk()
window2.geometry("450x520+450+30")
window2.resizable(0, 0)
window2.title("Menu")
backgroundFrame = Frame(window2, width = 450, height = 520 ,bg = "white")
backgroundFrame.pack()

keLogo = PhotoImage(file = "KE_logo.png")
pic1 = Label(window2, image = keLogo, width = 420, height = 200, bg = "white")
pic1.place(x = 20, y = 10)

def add_customer():
    window2.destroy()
    import AddUser

def add_unit():
    window2.destroy()
    import addunits

def generate_bill():
    window2.destroy()
    import generatebill

btn1 = Button(window2, text = "Add Consumer", bg = "orange", relief = "solid", bd = 1, command = add_customer)
btn1.place(x = 110, y = 250, width = 230, height = 70)

btn2 = Button(window2, text = "Add Units", bg = "orange", relief = "solid", bd = 1, command = add_unit)
btn2.place(x = 110, y = 370,  width = 230, height = 70)

window2.mainloop()