# import all (*) and message box (to send message boxes to users later) from tkinter lib
from tkinter import *
from tkinter import messagebox
# import Regular Expression (used for email validation) and OS (used for moving to the next screen from the current screen):
import re
import os

# Create the main window for the registration form (I name the object to be window), using tkinter (TK) class:
window = Tk()
# Set title, size, and background color for the form:
window.title("Welcome! A few steps ahead to become our gorgeous members...") # title shown at the top of the form
window.geometry('500x500') # size of the form: 500x500
window.configure(background="light pink")

# Create input fields: full name, password, confirm password, phone number, email, gender, country, skill:
v_fullName = StringVar()
v_passWord = StringVar()
v_confirm_psw = StringVar()
v_phoneNo = StringVar()
v_email = StringVar()
v_gender = IntVar()
v_country = StringVar()
v_skill = StringVar()

# Create label widgets, which implements a display box in which you can put texts or images.
# For the fields in which we ask users to type inputs in, also add entry widgets, which allow User to enter any kind of input (no., str, char..)

"""HEADING"""
lb_heading = Label(window, text="Registration Form", width=20, font=('normal', 25), bg='light pink')
lb_heading.place(x=80, y=53) # set the position of the heading (RECHECK)

"""FULL NAME"""
lb_fullName = Label(window, text="Full Name", width=15, font=('normal', 13), bg='salmon2')
lb_fullName.place(x=60, y=110)
# In order to create a box for the users to type in input, we need Entry:
entry_fullName = Entry(window, textvariable=v_fullName)
entry_fullName.place(x=220, y=110)
entry_fullName.configure(width=24)

"""PASSWORD"""
lb_passWord = Label(window, text="Password", width=15, font=('normal', 13), bg='salmon2')
lb_passWord.place(x=60, y=150)
entry_passWord = Entry(window, textvariable=v_passWord, show='*')
entry_passWord.place(x=220, y=150)
entry_passWord.configure(width=24)

"""CONFIRM PASSWORD"""
lb_confirm_psw = Label(window, text="Confirm Password", width=15, font=('normal', 13), bg='salmon2')
lb_confirm_psw.place(x=60, y=190)
entry_confirm_psw = Entry(window, textvariable=v_confirm_psw, show='*')
entry_confirm_psw.place(x=220, y=190)
entry_confirm_psw.configure(width=24)

"""For inputs that need validation (phone no., email), here are some steps to validate the inputs:
Step1: Create a validation function
Step2: Register the Callback validation function using func window.register
Step3: Give the option value
    a. validate (when to validate)
    b. validateCommand (what function to call)
    c. invalid comment (optional)"""

"""PHONE NUMBER"""
#Step1: Function for validation of Phone Number:
def validate_phoneNo(userPhoneNo):
    if userPhoneNo.isdigit() and len(userPhoneNo)==10:
        return True
    else:
        # messagebox.showinfo('Information', 'Only 10 digits are allowed for Phone Number.')
        return False

lb_phoneNo = Label(window, text="Phone Number", width=15, font=('normal', 13), bg='salmon2')
lb_phoneNo.place(x=60, y=230)
entry_phoneNo = Entry(window, textvariable=v_phoneNo)
entry_phoneNo.place(x=220, y=230)
entry_phoneNo.configure(width=24)
# Step2: Register the Callback validation function using func window.register
valid_phoneNo = window.register(validate_phoneNo) # create a var named valid_phoneNo to register the callback func


"""EMAIL"""
#Step1: Function for validation of email:
def validate_email(userEmail):
    if len(userEmail) < 8:
        messagebox.showinfo('Oops!', 'This is not a valid email.') # (Message title, Message body)
    else:
        if re.match(r"[^@]+@[^@]+\.[^@]+", userEmail) != None:
            return True
        else:
            messagebox.showinfo('Oops!', 'This is not a valid email.')
            return False
lb_email = Label(window, text="Email", width=15, font=('normal', 13), bg='salmon2')
lb_email.place(x=60, y=270)
entry_email = Entry(window, textvariable=v_email)
entry_email.place(x=220, y=270)
entry_email.configure(width=24)

"""GENDER"""
lb_gender = Label(window, text="Gender", width=15, font=('normal', 13), bg='salmon2')
lb_gender.place(x=60, y=310)
# Create radio button (the circle button):
Radiobutton(window, text='Male', bg='white', padx=5, variable=v_gender, value=1).place(x=220, y=310)
Radiobutton(window, text='Female', bg='white', padx=5, variable=v_gender, value=2).place(x=290, y=310)
Radiobutton(window, text="Other", bg='white', padx=5, variable=v_gender, value=3).place(x=375, y=310)

"""COUNTRY"""
lb_country = Label(window, text="Country", width=15, font=('normal', 13), bg='salmon2')
lb_country.place(x=60, y=350)
country_list = ['Vietnam', 'USA', 'England', 'China', 'Japan', 'Thailand', 'Malaysia', 'Singapore', 'Germany', 'India',
                'Afghanistan', 'Albania', 'Algeria', 'Australia', 'Austria']
# Create drop down list:
droplist = OptionMenu(window, v_country, *country_list) # whenever the user chooses his/her country,
                                                        # the input will be stored in the variable v_country.
                                                        # The star (*) before the country_list is for the countries to
                                                        # be shown vertically in the drop down list. Removing it will
                                                        # make them appear horizontally.
droplist.config(width=22, bg='white') # set the width and the background color of the drop list
v_country.set('Select your country') # what users see in the drop down list initally
droplist.place(x=220, y=350)


"""SKILLS"""
lb_skill = Label(window, text="Skill(s)", width=15, font=('normal', 13), bg='salmon2')
lb_skill.place(x=60, y=390)
skill1 = IntVar()
skill2 = IntVar()
skill3 = IntVar()
Checkbutton(window, text='Hiphop', bg='white', variable=skill1). place(x=220, y=390)
Checkbutton(window, text='House', bg='white', variable=skill2).place(x=297, y=390)
Checkbutton(window, text='Waack', bg='white', variable=skill3).place(x=370, y=390)


def validateAllFields():
    # .get func below is to get the input from the given key (e.g. v_fullName or v_passWord), if the input is present
    # in the library. If not, it will print "None". Syntax: Dict.get(key, default=None)
    # In case you want to change what it prints when the input is NOT present in the lib,
    # Dict.get(key, "Not found")
    if v_fullName.get() == "":
        messagebox.showinfo('You forget something...', 'Please enter your name.')
    elif v_passWord.get() == '':
        messagebox.showinfo('You forget something...', 'Please enter your password.')
    elif v_confirm_psw.get() == '':
        messagebox.showinfo('You forget something...', 'Please confirm your password.')
    elif v_passWord.get() != v_confirm_psw.get():
        messagebox.showinfo('Oops!', 'Password not match.')
    elif v_email.get() == "":
        messagebox.showinfo('You forget something...', 'Please enter your email address.')
    elif v_phoneNo.get() == '':
        messagebox.showinfo('You forget something...', 'Please enter your phone number.')
    elif v_gender.get() != 1 and v_gender.get() != 2 and v_gender.get() != 3:
        messagebox.showinfo('You forget something...', 'Please choose your gender.')
    elif v_country.get() == '' or v_country.get() == 'Select your country.':
        messagebox.showinfo('You forget something...', 'Please choose your country.')
    elif skill1.get() == 0 and skill2.get() == 0 and skill3.get() == 0:
        messagebox.showinfo('You forget something...', 'Please choose your skill(s).')
    elif v_phoneNo.get().isdigit() and len(v_phoneNo.get()) != 10: # STILL WORKING
        messagebox.showinfo('Oops!', 'Your phone number is not valid.')
    elif v_email.get() != '':
        valid_Email = validate_email(v_email.get())
        if valid_Email:
            messagebox.showinfo('Congratulation!', 'You have registered succesfully!')
    else:
        messagebox.showinfo('Congratulation!', 'You have registered succesfully!')

def clearAllFields():
    v_fullName.set("")
    v_passWord.set("")
    v_confirm_psw.set("")
    v_phoneNo.set("")
    v_email.set("")

def callNewScreen():
    window.destroy() # close the current window
    os.system('python logInScreen.py')

# Create 3 buttons at the end of the form which say "Register", "Clear all", or "Already an user?"
btn_register = Button(window, text='REGISTER', command=validateAllFields, bg='salmon2', fg='black',
                    font=('bold', 13)).place(x=100, y=440)
btn_clear = Button(window, text="CLEAR ALL", command=clearAllFields, bg='salmon2', fg='black',
                   font=('bold', 13)). place(x=190, y=440)
btn_alrUser = Button(window, text="ALREADY AN USER?", command=callNewScreen, bg='salmon2', fg='black',
                     font=('bold', 13)).place(x=290, y=440)


window.mainloop() # call the function endlessly so that the window remains open until the user closes it