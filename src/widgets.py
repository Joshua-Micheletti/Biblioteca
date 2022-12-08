from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter import StringVar
from tkinter import messagebox
from frames import *
from globalVars import *
from hashlib import sha256
from login import *

strings = dict()

# function to handle clicks
def clickHandler(*args):
    # login behaviour
    if args[0] == "login":
        if login(strings["usernameEntry"].get(), strings["passwordEntry"].get()):
            # set the login flag to true
            setLogin(True)
            # set the logged in user
            setUser(strings["usernameEntry"].get())
            # destroy the window (replace with function)
            getWindow().destroy()

        else:
            # notify the user that the login info is incorrect
            print("WRONG LOGIN INFO")
            messagebox.showerror("Login Error",
                                 "Error: wrong login info!")
    
    # register behaviour
    if args[0] == "register":
        if register(strings["usernameEntry"].get(), strings["passwordEntry"].get()):
            # let the user know of the registration
            messagebox.showinfo("Register Successful",
                                "The user " +
                                strings["usernameEntry"].get() +
                                " is now registered")
        
        else:
            # notify the user that the username already exists
            print("USERNAME ALREAD EXISTS")
            messagebox.showerror("Register Error",
                                 "Error: username already exists!")


# function to load widgets into the respective frames
def loadWidgets(frames):
    # login frame
    if "loginF" in frames:
        loadLogin(frames["loginF"])
    
    # app frame
    if "appF" in frames:
        loadApp(frames["appF"])


# FUNCTION TO LOAD WIDGETS TO FRAMES
# function to load the login window widgets
def loadLogin(frame):
    global widgets
    global strings

    # setup a stringvar for the username entry
    strings["usernameEntry"] = StringVar(name = "usernameEntry")
    # setup a stringvar for the password
    strings["passwordEntry"] = StringVar(name = "passwordEntry")


    # username label
    usernameLabel = Label(
        frame,
        text = "Username",
    )

    # create a username entry widget
    usernameEntry = Entry(
        frame,
        textvariable = strings["usernameEntry"],
    )
    usernameEntry.focus()

    # password label
    passwordLabel = Label(
        frame,
        text = "Password"
    )

    # create a password entry widget
    passwordEntry = Entry(
        frame,
        textvariable = strings["passwordEntry"],
        show = '*'
    )

    # create a button to login
    loginButton = Button(
        frame,
        text = "Login",
        command = lambda: clickHandler("login")
    )
    loginButton.state(["!disabled"])

    # create a button to register
    registerButton = Button(
        frame,
        text = "Register",
        command = lambda: clickHandler("register")
    )
    registerButton.state(["!disabled"])
    

    # position the widgets into the frame
    usernameLabel.grid(row = 0, column = 0, sticky = "s")
    usernameEntry.grid(row = 1, column = 0, sticky = "")

    passwordLabel.grid(row = 2, column = 0, sticky = "s")
    passwordEntry.grid(row = 3, column = 0)

    loginButton.grid(row = 4, column = 0, sticky = "s")
    registerButton.grid(row = 5, column = 0)

# function to load app window widgets
def loadApp(frame):
    print("App")
