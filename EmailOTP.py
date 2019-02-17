# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO GENERATE OTP, SEND IT TO USER-INPUT EMAIL-ID AND VALIDATE IT

# Importing necessary packages
import random
import smtplib
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Defining CreateWidgets() to create tkinter widgets
def CreateWidget():
    emailLabel = Label(root, text = "ENTER YOUR EMAIL-ID : ", bg = "grey")
    emailLabel.grid(row = 0, column = 1, padx = 5, pady = 5)

    emailEntry = Entry(root, textvariable = emailid, width = 30)
    emailEntry.grid(row = 0, column = 2, padx = 5, pady = 5)

    sendOTPbutton = Button(root, text = "Send OTP", command = sendOTP, width = 20)
    sendOTPbutton.grid(row = 0, column = 3, padx = 5, pady = 5)

    otpLabel = Label(root, text = "ENTER THE OTP : ", bg = "grey")
    otpLabel.grid(row = 1, column = 1, padx = 5, pady = 5)

    root.otpEntry = Entry(root, textvariable = otp, width = 30, show = "*")
    root.otpEntry.grid(row = 1, column = 2, padx = 5, pady = 5)

    validOTPbutton = Button(root, text = "Validate OTP", command = validOTP, width = 20)
    validOTPbutton.grid(row = 1, column = 3, padx = 5, pady = 5)

# Defining sendOTP() to generate and send OTP to user-input email-id
def sendOTP():

    numbers = "01234567890"
    root.genOTP = ""
    receiverEmail = emailid.get()

    # Generating 6-digits OTP
    for i in range(6):
        root.genOTP += numbers[int(random.random() * 10)]

    # Message to be sent
    otpMSG = "Your OTP is : " + root.genOTP

    # Creating instance of class MIMEMultipart()
    message = MIMEMultipart()

    # Storing the details in respective fields
    message['FROM'] = "OTP GENERATOR"
    message['Subject'] = "OTP VALIDATION"

    # Attach message with MIME instance
    message.attach(MIMEText(otpMSG))

    # Create a smtp session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # Starting TLS for security
    smtp.starttls()

    # Authenticate the user
    smtp.login("sender's email-id", "sender's password")

    # Sending the email with Mulitpart message converted into string
    smtp.sendmail("sender's email-id", receiverEmail, message.as_string())

    # Terminating the session
    smtp.quit()

    otpSendLabel = Label(root, text="OTP HAS BEEN SENT TO " + receiverEmail, bg = "grey")
    otpSendLabel.grid(row=2, column=1, padx=5, pady=5, columnspan = 3)

def validOTP():
    # Storing user-input OTP
    userInputOTP = otp.get()
    # Storing system generated OTP
    systemOTP = root.genOTP

    # Validating OTP
    if userInputOTP == systemOTP:
        messagebox.showinfo("SUCCESS"," OTP validated")
        root.otpEntry.delete('0','end')
    else:
        messagebox.showerror("ERROR", "Invalid OTP")
        root.otpEntry.delete('0', 'end')

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color
# and disabling the resizing property
root.title("EmailOTP")
root.resizable(False, False)
root.config(background = "grey")

# Creating tkinter variables
emailid = StringVar()
otp = StringVar()

# Calling the CreateWidgets() function with argument bgColor
CreateWidget()

# Defining infinite loop to run application
root.mainloop()