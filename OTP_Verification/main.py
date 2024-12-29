import random
import smtplib
from tkinter import *

def generateOTP():
    """Generate a 6-digit OTP."""
    return ''.join(str(random.randint(0, 9)) for _ in range(6))

# Email sender credentials
sender = "yoginath66t@gmail.com"  # sender  email
password = "glve rtyy klzn cuhy"  # sender app password
code = generateOTP()

def connectingSender():
    """Connect to the SMTP server and send the OTP."""
    receiver = receiverMail.get()
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        sendingMail(receiver, server)
    except Exception as e:
        errorLabel = Label(otp, text=f"Error: {e}", fg='red', font=('Arial', 12), bg='#FFF1DC')
        errorLabel.place(x=15, y=160)

def sendingMail(receiver, server):
    """Send the OTP to the receiver's email."""
    try:
        subject = "Your OTP Code"
        msg = f"Hello!\nYour OTP is: {code}\nPlease do not share it with anyone."
        server.sendmail(sender, receiver, msg)
        server.quit()
        successLabel = Label(otp, text="OTP sent successfully!", fg='green', font=('Arial', 12), bg='#FFF1DC')
        successLabel.place(x=15, y=160)
    except Exception as e:
        errorLabel = Label(otp, text=f"Error: {e}", fg='red', font=('Arial', 12), bg='#FFF1DC')
        errorLabel.place(x=15, y=160)

def checkOTP():
    """Verify the entered OTP."""
    if code == codeEntry.get():
        accept = Label(otp, text='ACESS GRANTED!', fg='green', font=('Arial', 20), bg='#FFF1DC')
        accept.place(x=230, y=350)
    else:
        refuse = Label(otp, text='ACCESS DENIED!', fg='red', font=('Arial', 20), bg='#FFF1DC')
        refuse.place(x=230, y=350)

# Create the GUI window
otp = Tk()
otp.title('OTP Verification')
otp.geometry('750x400')
otp.config(bg='#FFF1DC')

# Email input label and field
mailMsg = Label(otp, text="E-Mail", justify=LEFT, bg='#FFF1DC', font=("Arial", 16))
mailMsg.place(x=15, y=40)

receiverMail = Entry(otp, width=35, font=("Arial", 20), borderwidth=0)
receiverMail.place(x=100, y=40)

# Send OTP button
sendOTP = Button(otp, text="Send OTP", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="#AA5656", fg="black", command=connectingSender)
sendOTP.place(x=280, y=100)

# OTP input label and field
otpMsg = Label(otp, text="OTP", bg='#FFF1DC', font=('Arial', 16))
otpMsg.place(x=15, y=210)

codeEntry = Entry(otp, width=6, font=("Arial", 20), borderwidth=0)
codeEntry.place(x=100, y=210)

# Verify button
verify = Button(otp, text="Verify", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="#AA5656", fg="black", command=checkOTP)
verify.place(x=280, y=280)

otp.mainloop()

