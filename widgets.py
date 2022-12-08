from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter import StringVar
from frames import *
from globalVars import *

widgets = dict()
downloadIcon = None
strings = dict()

def clickFunction():
    print("clicked!")

def clickFunctionWithArgs(args):
    print(args)


def login(window):
    global loggedIn

    setLogin(True)
    checkLoggedIn()
    window.destroy()


def checked():
    global strings
    print("checked: " + strings["checkbox"].get())

def entryCallback(*args):
    print(strings[args[0]].get())

def changeTheme(theme, window):
    print(theme)
    window.set_theme(theme)



def loadWidgets(frames, window):
    if "loginF" in frames:
        loadLogin(frames["loginF"], window)
    
    if "appF" in frames:
        loadApp(frames["appF"], window)


def loadLogin(frame, window):
    global widgets
    global strings

    usernameLabel = Label(
        frame,
        text = "Username",
    )
    strings["usernameEntry"] = StringVar(name = "usernameEntry")
    strings["usernameEntry"].trace('w', entryCallback)
    usernameEntry = Entry(
        frame,
        textvariable = strings["usernameEntry"],
    )
    usernameLabel.grid(row = 0, column = 0, sticky = "s")
    usernameEntry.grid(row = 1, column = 0, sticky = "")
    usernameEntry.focus()
    widgets["usernameEntry"] = usernameEntry
    widgets["usernameLabel"] = usernameLabel

    passwordLabel = Label(
        frame,
        text = "Password"
    )
    strings["passwordEntry"] = StringVar(name = "passwordEntry")
    strings["passwordEntry"].trace('w', entryCallback)
    passwordEntry = Entry(
        frame,
        textvariable = strings["passwordEntry"],
        show = '*'
    )
    passwordLabel.grid(row = 2, column = 0, sticky = "s")
    passwordEntry.grid(row = 3, column = 0)
    widgets["passwordEntry"] = passwordEntry

    loginButton = Button(
        frame,
        text = "Login",
        command = lambda: login(window)
    )
    loginButton.state(["!disabled"])
    loginButton.grid(row = 4, column = 0, sticky = "s")
    widgets["loginButton"] = loginButton

    registerButton = Button(
        frame,
        text = "Register",
        command = lambda: clickFunctionWithArgs("Register")
    )
    registerButton.state(["!disabled"])
    registerButton.grid(row = 5, column = 0)
    widgets["registerButton"] = registerButton


def loadApp<(frame, window):
    print("App")

def loadButtons(frame, window):
    global widgets
    global downloadIcon

    # NORMAL BUTTON
    button = Button(
        frame,
        text = "Click Me",
        command = clickFunction
    )
    button.state(["!disabled"])
    button.pack(pady = 5)
    widgets["button"] = button

    downloadIcon = PhotoImage(file = "./data/download.png")

    # IMAGE BUTTON
    imageButton = Button(
        frame,
        image = downloadIcon,
        command = clickFunction
    )
    imageButton.pack(pady = 5)
    widgets["imageButton"] = imageButton

    # COMPOUND IMAGE + TEXT BUTTONS
    compoundFrame = Frame(frame)
    compoundFrame.pack()

    compoundButton = Button(
        compoundFrame,
        image = downloadIcon,
        text = "Download",
        compound = "left",
        command = clickFunction
    )
    compoundButton.grid(row = 0, column = 0, pady = 5, padx = 5)
    widgets["compoundButton"] = compoundButton

    compoundButtonRight = Button(
        compoundFrame,
        image = downloadIcon,
        text = "Download",
        compound = "right",
        command = clickFunction
    )
    compoundButtonRight.grid(row = 0, column = 1, pady = 5, padx = 5)
    widgets["compoundButtonRight"] = compoundButtonRight

    # BUTTON WITH CALLBACK ARGUMENTS
    argumentButton = Button(
        frame,
        text = "Print this string",
        command = lambda: clickFunctionWithArgs("this string")
    )
    argumentButton.pack(pady = 5)
    widgets["argumentButton"] = argumentButton


def loadCheckboxes(frame):
    global strings
    global widgets

    strings["checkbox"] = StringVar(name = "checkbox")

    checkbox = Checkbutton(
        frame,
        text = "Checkbox",
        command = checked,
        variable = strings["checkbox"],
        onvalue = "True",
        offvalue = "False"
    )
    checkbox.pack()
    widgets["checkbox"] = checkbox


def loadEntries(frame):
    global widgets
    global strings

    entryLabel = Label(
        frame,
        text = "Input"
    )
    strings["entry"] = StringVar(name = "entry")
    strings["entry"].trace('w', entryCallback)
    entry = Entry(
        frame,
        textvariable = strings["entry"],
    )
    entryLabel.pack()
    entry.pack(pady = (0, 5))
    entry.focus()
    widgets["entry"] = entry
    widgets["entryLabel"] = entryLabel

    passwordLabel = Label(
        frame,
        text = "Password"
    )
    strings["password"] = StringVar(name = "password")
    strings["password"].trace('w', entryCallback)
    password = Entry(
        frame,
        textvariable = strings["password"],
        show = '*'
    )
    passwordLabel.pack()
    password.pack(pady = (0, 5))
    widgets["password"] = password


def loadStyles(frame, window):
    row = 0
    buttonsPerRow = 4
    for i in range(len(window.get_themes())):
        if (i % buttonsPerRow == 0):
            row += 1

        button = Button(
            frame,
            text = window.get_themes()[i],
            command = lambda theme = window.get_themes()[i], window = window: changeTheme(theme, window),
        ).grid(column = i % buttonsPerRow, row = row, padx = 5, pady = 5)

        widgets["styleButton" + str(i)] = button


def loadLabels(frame):
    global widgets

    label = Label(
        frame,
        text = "Normal Label"
    )

    label.pack()
    widgets["label"] = label

    warningLabel = Label(
        frame,
        style = "Warning.TLabel",
        text = "Warning"
    )
    warningLabel.pack()
    widgets["warningLabel"] = warningLabel