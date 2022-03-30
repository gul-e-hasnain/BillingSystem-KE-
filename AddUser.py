from tkinter import *
from tkinter import messagebox
import csv

window3 = Tk()
window3.geometry("450x520+450+30")
window3.resizable(0, 0)
window3.title("Add Consumer")

backgroundFrame = Frame(window3, width = 450, height = 520 ,bg = "white")
backgroundFrame.pack()

userName = StringVar()
cnicNo = StringVar()
cntNo = StringVar()
userAddress = StringVar()
userEmail = StringVar()
radio_var = StringVar()

def validation():
    Username = userName.get()
    CNICNO = cnicNo.get()
    CNICNO = str(CNICNO)
    contactNo = cntNo.get()
    contactNo = str(contactNo)
    Useraddress = userAddress.get()
    Useremail = userEmail.get()
    radio = radio_var.get()
    ConsumerNo = StringVar()
    AccountNo = StringVar()

    if Username == "":
        messagebox.showerror("Alert", "User Name is required")
    elif CNICNO == "":
        messagebox.showerror("Alert", "CNIC Number is required")
    elif len(CNICNO) > 13 or len(CNICNO) < 13:
        messagebox.showerror("Alert", "Incorrect CNIC Number")
    elif contactNo == "":
        messagebox.showerror("Alert", "Contact Number is required")
    elif len(contactNo) > 11 or len(contactNo) < 11:
        messagebox.showerror("Alert", "Incorrect Contact Number")
    elif Useraddress == "":
        messagebox.showerror("Alert", "Address is required")
    elif Useremail == "":
        messagebox.showerror("Alert", "Email is required")
    elif radio == "":
        messagebox.showerror("Alert", "Select Type Of Connection")
    else:
        import random
        import string
        string.ascii_uppercase

        alpha = random.choice(string.ascii_uppercase)
        alpha1 = random.choice(string.ascii_uppercase)

        num = random.randrange(100000, 999999)

        ConsumerNo = alpha + alpha1 + str(num)

        import random
        AccountNo = random.randrange(1000000000000, 9999999999999)
        previousMeterReading = 0

        data_list = [Username, CNICNO, ConsumerNo, AccountNo, previousMeterReading ,radio, contactNo, Useraddress, Useremail]
        with open('New_Add_User.csv', 'a', newline='') as writefile:
            the_writer = csv.writer(writefile)

            the_writer.writerow(data_list)

        window3.destroy()
        import register

reg_text = Label(backgroundFrame, text = "Registration Form", fg = "black", font = ("arial", 25), bg = "white")
reg_text.place(x = 92, y = 50)

name = Label(backgroundFrame, text = "User Name: ", width = 20, font = ("bold",10), bg = "white")
name.place(x = 20, y = 130)

txtname = Entry(backgroundFrame, width = 30, textvar = userName, relief = "solid")
txtname.place(x = 180, y = 130)

cnic = Label(backgroundFrame, text = "CNIC Number: ", width = 20, font = ("bold",10), bg = "white")
cnic.place(x = 20, y = 180)

txtcnic = Entry(backgroundFrame, width = 30, textvar = cnicNo, relief = "solid")
txtcnic.place(x = 180, y = 180)

contactNumber = Label(backgroundFrame, text = "Contact Number: ", width = 20, font = ("bold",10), bg = "white")
contactNumber.place(x = 20, y = 230)

txtcontactNumber = Entry(backgroundFrame, width = 30, textvar = cntNo, relief = "solid")
txtcontactNumber.place(x = 180, y = 230)

address = Label(backgroundFrame, text = "Address: ", width = 20, font = ("bold",10), bg = "white")
address.place(x = 20, y = 280)

txtaddress = Entry(backgroundFrame, width = 30, textvar = userAddress, relief = "solid")
txtaddress.place(x = 180, y = 280)

email = Label(backgroundFrame, text = "Email: ", width = 20, font = ("bold",10), bg = "white")
email.place(x = 20, y = 330)

txtemail = Entry(backgroundFrame, width = 30, textvar = userEmail, relief = "solid")
txtemail.place(x = 180, y = 330)

type_label = Label(backgroundFrame, text = "Connection Type:", width = 20, font = ("bold", 10), bg = "white")
type_label.place(x = 20, y = 380)

radio_btn_1 = Radiobutton(backgroundFrame, text = "commercial", variable = radio_var, value = "commercial", bg = "white")
radio_btn_1.place(x = 180, y = 380)

radio_btn_2 = Radiobutton(backgroundFrame, text = "Residential", variable = radio_var, value = "residential", bg = "white")
radio_btn_2.place(x = 280, y = 380)

submit_btn = Button(backgroundFrame, text = "Submit", font = ("bold", 12), fg = "black", bg = "orange", width = 16, relief = "solid", bd = 1, command = validation)
submit_btn.place(x = 150, y = 440)

window3.mainloop()