# import all (*) and message box (to send message boxes to users later) from tkinter lib
from tkinter import *
from tkinter import messagebox
# import Regular Expression (used for email validation) and OS (used for moving to the next screen from the current screen):
import re
import os

# Create the main window for the registration form (I name the object to be window), using tkinter (TK) class:
window = Tk()
# Set title, size, and background color for the form:
window.title("Welcome to the Registration Form") # title shown at the top of the form
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
lb_heading = Label(window, text="Registration Form", width=20, font=('bold', 20), bg='light pink')
lb_heading.place(x=90, y=53) # set the position of the heading (RECHECK)

"""FULL NAME"""
lb_fullName = Label(window, text="Full Name:", width=10, font=('normal', 10), bg='light yellow')
lb_fullName.place(x=80, y=130)
# In order to create a box for the users to type in input, we need Entry:
entry_fullName = Entry(window, textvariable=v_fullName)
entry_fullName.place(x=240, y=130)

"""PASSWORD"""
lb_passWord = Label(window, text="Password:", width=10, font=('normal', 10), bg='salmon2')
lb_passWord.place(x=80, y=170)
entry_passWord = Entry(window, textvariable=v_passWord)
entry_passWord.place(x=240, y=170)

"""CONFIRM PASSWORD"""
lb_confirm_psw = Label(window, text="Confirm Password:", width=10, font=('normal', 10), bg='salmon2')
lb_confirm_psw.place(x=80, y=210)
entry_confirm_psw = Entry(window, textvariable=v_confirm_psw)
entry_confirm_psw.place(x=240, y=210)

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
    if userPhoneNo.isdigit():
        return True
    elif userPhoneNo == "":
        messagebox.showinfo('You forget something...', 'Add phone number.') # (Message title, Message body)
        return False
    else:
        messagebox.showinfo('Information', 'Only digits are allowed for Phone Number.')
        return False

lb_phoneNo = Label(window, text="Phone Number:", width=10, font=('normal', 10), bg='IndianRed3')
lb_phoneNo.place(x=80, y=250)
entry_phoneNo = Entry(window, textvariable=v_phoneNo)
entry_phoneNo.place(x=240, y=250)
# Step2: Register the Callback validation function using func window.register
valid_phoneNo = window.register(validate_phoneNo) # create a var named valid_phoneNo to register the callback func
# Step3: Give the option value
#     a. validate (when to validate): whenever a key is pressed on the "Phone number" field
#     b. validateCommand (what function to call): validate_phoneNo
#     c. invalid comment (optional)
"""%P, or percentage specifier, is used to pass inputs into our callback function."""
# entry_phoneNo.config(validate="key", validateCommand=(valid_phoneNo, '%P'))

"""EMAIL"""
#Step1: Function for validation of email:
def validate_email(userEmail):
    if len(userEmail) < 8:
        messagebox.showinfo('Oops!', 'This is not a valid email.')
    else:
        # if re.match('^[_a-z0-9-] + (\.[_a-z0-9-])*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z](2,4))$', userEmail) != None:
        #     return True
        # else:
        #     messagebox.showinfo('Oops!', 'This is not a valid email.')
        return False
lb_email = Label(window, text="Email:", width=10, font=('normal', 10), bg='light green')
lb_email.place(x=80, y=290)
entry_email = Entry(window, textvariable=v_email)
entry_email.place(x=240, y=290)

"""GENDER"""
lb_gender = Label(window, text="Gender:", width=10, font=('normal', 10), bg='orange')
lb_gender.place(x=80, y=330)
# Create radio button (the circle button):
Radiobutton(window, text='Male', bg='orange', padx=5, variable=v_gender, value=1).place(x=230, y=330)
Radiobutton(window, text='Female', bg='orange', padx=5, variable=v_gender, value=2).place(x=290, y=330)
Radiobutton(window, text="Other", bg='orange', padx=5, variable=v_gender, value=3).place(x=350, y=330)

"""COUNTRY"""
lb_country = Label(window, text="Country:", width=10, font=('normal', 10), bg='light cyan')
lb_country.place(x=80, y=370)
country_list = ['Vietnam', 'USA', 'England', 'China', 'Japan', 'Thailand', 'Malaysia', 'Singapore', 'Germany', 'India',
                'Afghanistan', 'Albania', 'Algeria', 'Australia', 'Austria']
# Create drop down list:
droplist = OptionMenu(window, v_country, *country_list) # whenever the user chooses his/her country,
                                                        # the input will be stored in the variable v_country.
                                                        # The star (*) before the country_list is for the countries to
                                                        # be shown vertically in the drop down list. Removing it will
                                                        # make them appear horizontally.
droplist.config(width=16, bg='light cyan') # set the width and the background color of the drop list
v_country.set('Select your country.') # what users see in the drop down list initally
droplist.place(x=240, y=370)

"""SKILLS"""
lb_skill = Label(window, text="Skill(s):", width=10, font=('normal', 10), bg='lavender')
lb_skill.place(x=80, y=410)
skill1 = IntVar()
skill2 = IntVar()
skill3 = IntVar()
Checkbutton(window, text='Hiphop', bg='lavender', variable=skill1). place(x=230, y=410)
Checkbutton(window, text='House', bg='lavender', variable=skill2).place(x=300, y=410)
Checkbutton(window, text='Waack', bg='lavender', variable=skill3).place(x=370, y=410)

# Create 3 buttons at the end of the form which say "Register", "Clear all", or "Already an user?"

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
    # elif v_phoneNo.get() != '':
    #     isValidphoneNo = validate_phoneNo(v_phoneNo.get())
    #     if isValidphoneNo:
    #         return True
    #     else:
    #         messagebox.showinfo('Oops!', 'Your phone number is not valid.')
    elif len(v_phoneNo.get()) != 10:
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
    os.system('LoginScreen.py') # use os.system('LoginScreen.py') in the same file
                                      # if not, use os.system('python LoginScreen.py')

btn_register = Button(window, text='REGISTER', command=validateAllFields, bg='deep pink', fg='black',
                    font=('bold', 10)).place(x=150, y=450)
btn_clear = Button(window, text="CLEAR ALL", command=clearAllFields, bg='deep pink', fg='black',
                   font=('bold', 10)). place(x=250, y=450)
btn_alrUser = Button(window, text="ALREADY AN USER?", command=callNewScreen, bg='deep pink', fg='black',
                     font=('bold', 10)).place(x=350, y=450)


window.mainloop() # call the function endlessly until the user closes it