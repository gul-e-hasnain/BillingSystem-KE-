from tkinter import *
from tkinter import messagebox
import csv

window4 = Tk()
window4.geometry("450x520+450+30")
window4.resizable(0, 0)
window4.title("Add User")

backgroundFrame = Frame(window4, width=450, height=520, bg="white")
backgroundFrame.pack()

global unit
Cnicno = StringVar()
consumerNo = StringVar()
accountNo = StringVar()
meterReading = IntVar()
pmeterReading = StringVar()
Units = StringVar()
var = StringVar()
global UserName, UserAddress, CnicNo, ContractNo, Consumerno, ConnectionType, AccountNo, Unit
def checK():
    global UserName, UserAddress, CnicNo, ContractNo, Consumerno, ConnectionType, AccountNo, Unit
    CnicNo = Cnicno.get()
    meterreading = meterReading.get()

    csv_file = csv.reader(open("records.csv", 'r'))

    if CnicNo == "":
        messagebox.showerror("Alert", "CNIC Number is required")
    else:
        for row in csv_file:
            if CnicNo == row[1]:
                UserName = row[0]
                UserAddress = row[7]
                ContractNo = row[9]
                AccountNo = row[3]
                txtconsumer_No.insert(0, row[2])
                Consumerno = row[2]
                txtaccount_No.insert(0, row[3])
                txtp_meter_reading.insert(0, row[4])
                p = txtp_meter_reading.get()
                txtunit.insert(0, meterreading - int(p))
                Unit = Units.get()
                ConnectionType = row[5]

    return

def generate_bill():
     window4.destroy()

     import time
     from PIL import ImageTk, Image, ImageDraw

     root = Tk()
     root.title("Bill")
     root.geometry("610x610+450+30")
     root.resizable(0, 0)
     root.configure(background="white")

     canvas = Canvas(root,width = 600, height = 600)
     image = ImageTk.PhotoImage(Image.open("bill.png"))

     canvas.create_image(0, 0, anchor = NW, image = image)
     canvas.pack()

     canvas.create_text(40, 65, text = UserName)
     canvas.create_text(52, 80, text = UserAddress)
     canvas.create_text(47, 95, text = 'CNIC No.')
     canvas.create_text(100, 95, text = CnicNo)
     canvas.create_text(56, 109, text = 'Contract No.')
     canvas.create_text(120, 109, text = ContractNo)
     canvas.create_text(64, 124, text = "Consumer No.")
     canvas.create_text(138, 124, text = Consumerno)
     canvas.create_text(50, 152, text = ConnectionType)
     canvas.create_text(350, 130, text = AccountNo)
     canvas.create_text(250, 550, text = AccountNo)
     canvas.create_text(244, 538, text = UserName)
     canvas.create_text(60, 185, text = Unit + ' ' + "Units", font = ('bold'))

     billing_month = time.strftime("%b-%y")
     canvas.create_text(555, 152, text = billing_month)

     issue_date = time.strftime("07-%b-%y")
     canvas.create_text(462, 152, text = issue_date)

     due_date = time.strftime("   21st  \n%B\n  %Y")
     canvas.create_text(540, 250, text = due_date)

     due_date2 = time.strftime("21-%b-%y")
     canvas.create_text(557, 515, text = due_date2)

     #-------Amount Calculation --------

     import math
     Unit_Used = int(Unit)

     if Unit_Used <= 300:
         electricity_charges = float(Unit_Used * 10.2)
         gst = electricity_charges * 0.176
         electricity_Duty = electricity_charges * 0.05
         fee = 35
         government_charges = gst + electricity_Duty + fee
         total_Bill = math.ceil(government_charges + electricity_charges)
         #print(total_Bill)

         late_fee = math.ceil(total_Bill * 0.085)
         late_Bill = late_fee + total_Bill

         #print(late_fee)
         #print(late_Bill)

     elif Unit_Used > 300 and Unit_Used <= 700:
         temp = float(Unit_Used - 300)
         extra = temp
         temp = float(temp * 17.6)
         electricity_charges = temp + (300 * 10.2)

         gst = electricity_charges * 0.176
         electricity_Duty = electricity_charges * 0.05
         fee = 35
         goverment_Charges = gst + electricity_Duty + fee
         total_Bill = math.ceil(goverment_Charges + electricity_charges)
         #print(total_Bill)

         late_fee = math.ceil(total_Bill * 0.085)
         late_Bill = late_fee + total_Bill

         #print(late_fee)
         #print(late_Bill)

     else:
         temp = float(Unit_Used - 700)
         extra = Unit_Used - temp
         temp = float(temp * 20.70)

         temp2 = float(extra - 300)
         extra2 = (Unit_Used - (temp2 + temp))
         temp2 = float(temp2 * 17.6)

         electricity_charges = temp + temp2 + (extra2 * 10.2)

         gst = electricity_charges * 0.176
         electricity_Duty = electricity_charges * 0.05
         fee = 35
         goverment_Charges = gst + electricity_Duty + fee
         total_Bill = math.ceil(goverment_Charges + electricity_charges)
         #print(total_Bill)

         late_fee = math.ceil(total_Bill * 0.085)
         late_Bill = late_fee + total_Bill

         #print(late_fee)
         #print(late_Bill)

     #--------------------------------------

     canvas.create_text(350, 185, text = 'Rs.' + ' ' + str(total_Bill), font = ('bold'))
     canvas.create_text(340, 545, text = 'Rs.' + ' ' + str(total_Bill))
     canvas.create_text(350, 255, text = 'Rs.' + ' ' + str(late_fee), font = ('bold'))
     canvas.create_text(350, 315, text = 'Rs.' + ' ' + str(late_Bill), font = ('bold'))
     canvas.create_text(560, 543, text = 'Rs.' + " " + str(late_Bill))

     canvas.create_text(150, 230, text = "---------------------------------------------------")
     canvas.create_text(150, 250, text = "---------------------------------------------------")
     canvas.create_text(70, 260, text = "Variable Charges")
     #canvas.create_text(150, 240, text = "Units")
     canvas.create_text(220, 240, text = "Rate/Unit")
     canvas.create_text(43, 280, text = "0 - 300")
     canvas.create_text(220, 280, text = "10.20")
     canvas.create_text(48, 300, text = '301 - 700')
     canvas.create_text(220, 300, text = '17.60')
     canvas.create_text(150, 310, text="---------------------------------------------------")
     canvas.create_text(65, 325, text = 'Electricity Duty')
     canvas.create_text(270, 325, text = "5%")
     canvas.create_text(70, 345, text = 'General Sales Tax')
     canvas.create_text(270, 345, text = '17.6%')
     canvas.create_text(45 , 365, text = 'TVL Fes')
     canvas.create_text(270, 365, text = 'Rs. 35')
     canvas.create_text(150, 375, text="---------------------------------------------------")

     root.mainloop()
     return

reg_text = Label(backgroundFrame, text="       Add Units", fg="black", font=("arial", 25), bg="white")
reg_text.place(x=92, y=10)

CNIC = Label(backgroundFrame, text="CNIC No: ", width=20, font=("bold", 10), bg="white")
CNIC.place(x=20, y=80)
CNIC = Entry(backgroundFrame, width=30, textvar=Cnicno, relief="solid")
CNIC.place(x=180, y=80)

meter_reading = Label(backgroundFrame, text="Meter Reading: ", width=20, font=("bold", 10), bg="white")
meter_reading.place(x=20, y=140)
txtmeter_reading = Entry(backgroundFrame, width=30, textvar=meterReading, relief="solid")
txtmeter_reading.place(x=180, y=140)

load_btn = Button(backgroundFrame, text="Load", font=("bold", 12), fg="black", bg="orange", width=16, relief="solid",bd=1, command = checK)
load_btn.place(x=180, y=190)

consumer_No = Label(backgroundFrame, text="Consumer Number: ", width=20, font=("bold", 10), bg="white")
consumer_No.place(x=20, y=260)
txtconsumer_No = Entry(backgroundFrame, width=30, textvar=consumerNo, relief="solid")
txtconsumer_No.place(x=180, y=260)

account_No = Label(backgroundFrame, text="Account No: ", width=20, font=("bold", 10), bg="white")
account_No.place(x=20, y=310)
txtaccount_No = Entry(backgroundFrame, width=30, textvar=accountNo, relief="solid")
txtaccount_No.place(x=180, y=310)

p_meter_reading = Label(backgroundFrame, text=" Previous Meter Reading: ", width=20, font=("bold", 10), bg="white")
p_meter_reading.place(x=20, y=360)
txtp_meter_reading = Entry(backgroundFrame, width=30, textvar=pmeterReading, relief="solid")
txtp_meter_reading.place(x=180, y=360)

unit = Label(backgroundFrame, text=" Units: ", width=20, font=("bold", 10), bg="white")
unit.place(x=20, y=410)
txtunit = Entry(backgroundFrame, width=30, textvar=Units, relief="solid")
txtunit.place(x=180, y=410)

bill_btn = Button(backgroundFrame, text="Generate Bill", font=("bold", 12), fg="black", bg="orange", width=16, relief="solid", bd=1, command = generate_bill)
bill_btn.place(x=180, y=460)

window4.mainloop()