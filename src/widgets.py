from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter import StringVar
from tkinter import messagebox
from frames import *
from globalVars import *
from hashlib import sha256
from login import *
from window import *

widgets = dict()

# function to handle clicks
def clickHandler(*args):
    print(args[0])

    # login behaviour
    if args[0] == "login":
        if login(getStrings()["usernameEntry"].get(), getStrings()["passwordEntry"].get()):
            # set the login flag to true
            setLogin(True)
            # set the logged in user
            setUser(getStrings()["usernameEntry"].get())
            # destroy the window (replace with function)
            getWindow().destroy()

        else:
            # notify the user that the login info is incorrect
            print("WRONG LOGIN INFO")
            messagebox.showerror("Login Error",
                                 "Error: wrong login info!")
    
    # register behaviour
    if args[0] == "register":
        if register(getStrings()["usernameEntry"].get(), getStrings()["passwordEntry"].get()):
            # let the user know of the registration
            messagebox.showinfo("Register Successful",
                                "The user " +
                                getStrings()["usernameEntry"].get() +
                                " is now registered")
        
        else:
            # notify the user that the username already exists
            print("USERNAME ALREAD EXISTS")
            messagebox.showerror("Register Error",
                                 "Error: username already exists!")


    if args[0] == "logout":
        setLogin(False)
        setUser("")
        getWindow().destroy()


    if args[0] == "close":
        closeProgram()


    if args[0] == "search":
        createSearchWindow()


def switchView():
    value = getInts()["showRadio"].get()
    print(value)

def selectedBook(event):
    selectedBooks = []

    for selected_item in widgets["books"].selection():
        item = widgets["books"].item(selected_item)

        selectedBooks.append(item['values'])

        #record = item['values']
        # show a message
        #messagebox.showinfo(title='Information', message=','.join(record))

    print(selectedBooks)


# function to load widgets into the respective frames
def loadWidgets(frames):
    # login frame
    if "loginF" in frames:
        loadLogin(frames["loginF"])
    
    # app frame
    if "appF" in frames:
        loadApp(frames["appF"])

    if "appFUserInfo" in frames:
        loadAppUserInfo(frames["appFUserInfo"])
    
    if "appFDisplayOptions" in frames:
        loadAppDisplayOptions(frames["appFDisplayOptions"])
    
    if "appFSearch" in frames:
        loadAppSearch(frames["appFSearch"])
    
    if "appFDatabase" in frames:
        loadAppDatabase(frames["appFDatabase"])
    '''
    if "appFCC" in frames:
        loadAppCC(frames["appFCC"])

    if "appFCE" in frames:
        loadAppCE(frames["appFCE"])
    '''
    if "appFLogout" in frames:
        loadAppLogout(frames["appFLogout"])
    '''
    if "appFSC" in frames:
        loadAppSC(frames["appFSC"])

    if "appFSE" in frames:
        loadAppSE(frames["appFSE"])
    '''

    if "searchFrame" in frames:
        loadSearch(frames["searchFrame"])

# FUNCTION TO LOAD WIDGETS TO FRAMES
# function to load the login window widgets
def loadLogin(frame):
    # setup a stringvar for the username entry
    getStrings()["usernameEntry"] = StringVar(name = "usernameEntry")
    # setup a stringvar for the password
    getStrings()["passwordEntry"] = StringVar(name = "passwordEntry")


    # username label
    usernameLabel = Label(
        frame,
        text = "Username",
    )

    # create a username entry widget
    usernameEntry = Entry(
        frame,
        textvariable = getStrings()["usernameEntry"],
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
        textvariable = getStrings()["passwordEntry"],
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
    print("app")
    

def loadAppUserInfo(frame):
    getStrings()["booksOwned"] = StringVar(name = "booksOwned")
    getStrings()["booksOwned"].set("Libri: " + str(getBooksOwned()))


    userLabel = Label(
        frame,
        text = "User: " + getUser(),
    )

    booksLabel = Label(
        frame,
        textvariable = getStrings()["booksOwned"]
    )

    userLabel.pack(pady = (10, 0), padx = (10, 0), anchor = W)
    booksLabel.pack(pady = (0, 10), padx = (10, 0), anchor = W)


def loadAppDisplayOptions(frame):
    getInts()["showRadio"] = IntVar(name = "showRadio")
    getInts()["showRadio"].set(0)

    showLabel = Label(
        frame,
        text = "Mostra: "
    )

    libraryRadio = Radiobutton(
        frame,
        text = "Libreria",
        variable = getInts()["showRadio"],
        value = 0,
        command = switchView
    )

    ownedRadio = Radiobutton(
        frame,
        text = "Posseduti",
        variable = getInts()["showRadio"],
        value = 1,
        command = switchView
    )

    showLabel.pack(side = LEFT, padx = (30, 0))
    libraryRadio.pack(side = LEFT)
    ownedRadio.pack(side = LEFT)


def loadAppSearch(frame):
    searchButton = Button(
        frame,
        text = "Search",
        command = lambda: clickHandler("search")
    )

    searchButton.pack(padx = 10, pady = 15)


def loadAppDatabase(frame):    
    result = sendMySQL("SELECT * FROM libri;")

    columns = ('genere', 'titolo', 'autore', 'casaeditrice', 'anno', 'luogo')

    books = Treeview(
        frame,
        columns = columns,
        show = 'headings'
    )

    books.heading('genere', text="Genere")
    books.heading('titolo', text="Titolo")
    books.heading('autore', text="Autore")
    books.heading('casaeditrice', text="Casa Editrice")
    books.heading('anno', text="Anno")
    books.heading('luogo', text="Luogo")

    for i in range(len(result)):
        books.insert('', END, values = (
            result[i][0],
            result[i][1],
            result[i][2],
            result[i][3],
            result[i][4],
            result[i][5],
        ))

    scrollbar = Scrollbar(frame, orient=VERTICAL, command=books.yview)
    books.configure(yscroll=scrollbar.set)

    books.bind('<<TreeviewSelect>>', selectedBook)
    
    books.pack(expand = True, fill = "both", side = LEFT)
    scrollbar.pack(side = LEFT, fill = Y)
    
    widgets["books"] = books


def loadAppLogout(frame):

    closeButton = Button(
        frame,
        text = "Close",
        command = lambda: clickHandler("close")
    )

    logoutButton = Button(
        frame,
        text = "Logout",
        command = lambda: clickHandler("logout")
    )


    closeButton.pack(padx = 10, pady = 10, side = LEFT)
    logoutButton.pack(padx = 10, pady = 10, side = LEFT)


def loadSearch(frame):
    closeButton = Button(
        frame,
        text = "Close",
        command = lambda: getSearchWindow().destroy()
    ).pack()

