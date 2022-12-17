from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter import StringVar
from tkinter import messagebox
from tkinter import *
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
            
            createAppWindow()
            loadWidgets(loadAppFrames())

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

        if getSearchWindow() != None:
            closeSearchWindow()
        if getBookWindow() != None:
            closeBookWindow()

        getWindow().destroy()
        
        createLoginWindow()
        loadWidgets(loadLoginFrames())
        
        
    if args[0] == "close":
        getWindow().destroy()


    if args[0] == "search":
        if getSearchWindow() is None:
            createSearchWindow()
            loadWidgets(loadSearchFrames())

                
    if args[0] == "searchQuery":
        children = widgets["books"].get_children()
        for child in children:
            widgets["books"].delete(child)

        query = "SELECT * FROM libri "

        where = True
            
        if "genereEntry" in getStrings():
            if getStrings()["genereEntry"].get() != "":
                query += "WHERE Genere LIKE '%" + getStrings()["genereEntry"].get() + "%' "
                where = False

            if getStrings()["titoloEntry"].get() != "":
                if where:
                    query += "WHERE Titolo LIKE '%" + getStrings()["titoloEntry"].get() + "%' "
                    where = False
                else:
                    query += "AND Titolo LIKE '%" + getStrings()["titoloEntry"].get() + "%' "

            if getStrings()["autoreEntry"].get() != "":
                if where:
                    query += "WHERE Autore LIKE '%" + getStrings()["autoreEntry"].get() + "%' "
                    where = False
                else:
                    query += "AND Autore LIKE '%" + getStrings()["autoreEntry"].get() + "%' "

            if getStrings()["casaeditriceEntry"].get() != "":
                if where:
                    query += "WHERE CasaEditrice LIKE '%" + getStrings()["casaeditriceEntry"].get() + "%' "
                    where = False
                else:
                    query += "AND CasaEditrice LIKE '%" + getStrings()["casaeditriceEntry"].get() + "%' "

            if getStrings()["annoEntry"].get() != "":
                if where:
                    query += "WHERE Anno LIKE '%" + getStrings()["annoEntry"].get() + "%' "
                    where = False
                else:
                    query += "AND Anno LIKE '%" + getStrings()["annoEntry"].get() + "%' "

            if getStrings()["luogoEntry"].get() != "":
                if where:
                    query += "WHERE Luogo LIKE '%" + getStrings()["luogoEntry"].get() + "%' "
                    where = False
                else:
                    query += "AND Luogo LIKE '%" + getStrings()["luogoEntry"].get() + "%' "


        query += ";"

        result = sendMySQL(query)

        for i in range(len(result)):
            widgets["books"].insert('', END, values = (
                result[i][0],
                result[i][1],
                result[i][2],
                result[i][3],
                result[i][4],
                result[i][5],
            ))


    if args[0] == "searchClose":
        closeSearchWindow()

    
    if args[0] == "searchClear":
        getStrings()["genereEntry"].set("")
        getStrings()["titoloEntry"].set("")
        getStrings()["autoreEntry"].set("")
        getStrings()["casaeditriceEntry"].set("")
        getStrings()["annoEntry"].set("")
        getStrings()["luogoEntry"].set("")


    if args[0] == "addBook":
        if getBookWindow() is None:
            createBookWindow()
            loadWidgets(loadBookFrames("add"))
    

    if args[0] == "modifyBook":
        if len(widgets["books"].selection()) == 0:
            messagebox.showerror("Selection Error",
                                 "No book selected")
            return()

        if getBookWindow() is None:
            createBookWindow()
            loadWidgets(loadBookFrames("modify"))

            item = widgets["books"].item(widgets["books"].selection()[0])
            values = item['values']

            getStrings()["newGenereEntry"].set(values[0])
            getStrings()["newTitoloEntry"].set(values[1])
            getStrings()["newAutoreEntry"].set(values[2])
            getStrings()["newCasaeditriceEntry"].set(values[3])
            getStrings()["newAnnoEntry"].set(values[4])
            getStrings()["newLuogoEntry"].set(values[5])

    
    if args[0] == "removeBook":
        if len(widgets["books"].selection()) == 0:
            messagebox.showerror("Selection Error",
                                 "No book selected")
            return()

        for selected_item in widgets["books"].selection():
            item = widgets["books"].item(selected_item)
            values = item['values']
            
            for i in range(len(values)):
                if i != 4:
                    values[i] = values[i].replace("'", "''")

            sendMySQL("DELETE FROM libri " +
                      "WHERE Genere = '" + values[0] + "' " +
                      "AND Titolo = '" + values[1] + "' " +
                      "AND Autore = '" + values[2] + "' " +
                      "AND CasaEditrice = '" + values[3] + "' " +
                      "AND Anno = '" + str(values[4]) + "' " +
                      "AND Luogo = '" + values[5] + "';")

        clickHandler("searchQuery")          


    if args[0] == "addBookSQL":
        columns = []
        values = []

        if getStrings()["newGenereEntry"].get() != "":
            columns.append("Genere")
            values.append(getStrings()["newGenereEntry"].get())

        if getStrings()["newTitoloEntry"].get() != "":
            columns.append("Titolo")
            values.append(getStrings()["newTitoloEntry"].get())

        if getStrings()["newAutoreEntry"].get() != "":
            columns.append("Autore")
            values.append(getStrings()["newAutoreEntry"].get())

        if getStrings()["newCasaeditriceEntry"].get() != "":
            columns.append("CasaEditrice")
            values.append(getStrings()["newCasaeditriceEntry"].get())

        if getStrings()["newAnnoEntry"].get() != "":
            columns.append("Anno")
            values.append(getStrings()["newAnnoEntry"].get())

        if getStrings()["newLuogoEntry"].get() != "":
            columns.append("Luogo")
            values.append(getStrings()["newLuogoEntry"].get())

        if len(columns) == 0:
            messagebox.showerror("Insert Error",
                                 "No book info provided")
            return()

        tableColumns = ""
        tableValues = ""

        for i in range(len(columns)):
            tableColumns += columns[i]
            tableValues += "'" + values[i] + "'"

            if i != len(columns) - 1:
                tableColumns += ", "
                tableValues += ", "

        sendMySQL("INSERT INTO libri(" + tableColumns + ") " +
                  "VALUES (" + tableValues + ");")

        clickHandler("searchQuery")


    if args[0] == "modifyBookSQL":
        oldGenere = widgets["books"].item(widgets["books"].selection())["values"][0].replace("'", "''")
        oldTitolo = widgets["books"].item(widgets["books"].selection())["values"][1].replace("'", "''")
        oldAutore = widgets["books"].item(widgets["books"].selection())["values"][2].replace("'", "''")
        oldCasaeditrice = widgets["books"].item(widgets["books"].selection())["values"][3].replace("'", "''")
        oldAnno = str(widgets["books"].item(widgets["books"].selection())["values"][4])
        oldLuogo = widgets["books"].item(widgets["books"].selection())["values"][5].replace("'", "''")
        
        columns = []
        
        if getStrings()["newGenereEntry"] != "":
            columns.append("Genere = '" + getStrings()["newGenereEntry"].get().replace("'", "''") + "'")
        if getStrings()["newTitoloEntry"] != "":
            columns.append("Titolo = '" + getStrings()["newTitoloEntry"].get().replace("'", "''") + "'")
        if getStrings()["newAutoreEntry"] != "":
            columns.append("Autore = '" + getStrings()["newAutoreEntry"].get().replace("'", "''") + "'")
        if getStrings()["newCasaeditriceEntry"] != "":
            columns.append("CasaEditrice = '" + getStrings()["newCasaeditriceEntry"].get().replace("'", "''") + "'")
        if getStrings()["newAnnoEntry"] != "":
            columns.append("Anno = '" + getStrings()["newAnnoEntry"].get().replace("'", "''") + "'")
        if getStrings()["newLuogoEntry"] != "":
            columns.append("Luogo = '" + getStrings()["newLuogoEntry"].get().replace("'", "''") + "'")
            
        command = ""
            
        for i in range(len(columns)):
            if i != len(columns) - 1:
                command += columns[i] + ", "
            else:
                command += columns[i] + " "
        
        sendMySQL("UPDATE libri " +
                  "SET " + command +
                  "WHERE Genere = '" + oldGenere + "' " +
                  "AND Titolo = '" + oldTitolo + "' " + 
                  "AND Autore = '" + oldAutore + "' " + 
                  "AND CasaEditrice = '" + oldCasaeditrice + "' " + 
                  "AND Anno = '" + oldAnno + "' " + 
                  "AND Luogo = '" + oldLuogo + "' "
        )
        
        clickHandler("searchQuery")


    if args[0] == "closeBook":
        closeBookWindow()

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

    item = widgets["books"].item(widgets["books"].selection()[0])
    values = item['values']

    '''
    getStrings()["newGenereEntry"].set(values[0])
    getStrings()["newTitoloEntry"].set(values[1])
    getStrings()["newAutoreEntry"].set(values[2])
    getStrings()["newCasaeditriceEntry"].set(values[3])
    getStrings()["newAnnoEntry"].set(values[4])
    getStrings()["newLuogoEntry"].set(values[5])
    '''


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
    '''
    if "appFModifyLibrary" in frames:
        loadAppModifyLibrary(frames["appFModifyLibrary"])

    if "searchFrame" in frames:
        loadSearch(frames["searchFrame"])

    if "searchButtonsFrame" in frames:
        loadSearchButtons(frames["searchButtonsFrame"])

    if "bookFrame" in frames:
        loadBook(frames["bookFrame"])

    if "bookAddFrame" in frames:
        loadBookAdd(frames["bookAddFrame"])

    if "bookModifyFrame" in frames:
        loadBookModify(frames["bookModifyFrame"])

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

    searchButton.pack(side = RIGHT, padx = 10, pady = 15)


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

    if result != None:
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


def loadAppModifyLibrary(frame):
    addButton = Button(
        frame,
        text = "Add Book",
        command = lambda: clickHandler("addBook")
    )

    removeButton = Button(
        frame,
        text = "Remove Book",
        command = lambda: clickHandler("removeBook")
    )

    modifyButton = Button(
        frame,
        text = "Modify Book",
        command = lambda: clickHandler("modifyBook")
    )


    addButton.pack(side = RIGHT, padx = 10)
    removeButton.pack(side = RIGHT, padx = 10)
    modifyButton.pack(side = RIGHT, padx = 10)


def loadSearch(frame):
    if not "genereEntry" in getStrings():
        getStrings()["genereEntry"] = StringVar(name = "genereEntry")
    if not "titoloEntry" in getStrings():
        getStrings()["titoloEntry"] = StringVar(name = "titoloEntry")
    if not "autoreEntry" in getStrings():
        getStrings()["autoreEntry"] = StringVar(name = "autoreEntry")
    if not "casaeditriceEntry" in getStrings():
        getStrings()["casaeditriceEntry"] = StringVar(name = "casaeditriceEntry")
    if not "annoEntry" in getStrings():
        getStrings()["annoEntry"] = StringVar(name = "annoEntry")
    if not "luogoEntry" in getStrings():
        getStrings()["luogoEntry"] = StringVar(name = "luogoEntry")

    genereLabel = Label(
        frame,
        text = "Genere"
    )
    genereEntry = Entry(
        frame,
        textvariable = getStrings()["genereEntry"]
    )

    titoloLabel = Label(
        frame,
        text = "Titolo"
    )
    titoloEntry = Entry(
        frame,
        textvariable = getStrings()["titoloEntry"]
    )

    autoreLabel = Label(
        frame,
        text = "Autore"
    )
    autoreEntry = Entry(
        frame,
        textvariable = getStrings()["autoreEntry"]
    )

    casaeditriceLabel = Label(
        frame,
        text = "Casa Editrice"
    )
    casaeditriceEntry = Entry(
        frame,
        textvariable = getStrings()["casaeditriceEntry"]
    )

    annoLabel = Label(
        frame,
        text = "Anno"
    )
    annoEntry = Entry(
        frame,
        textvariable = getStrings()["annoEntry"]
    )

    luogoLabel = Label(
        frame,
        text = "Luogo"
    )
    luogoEntry = Entry(
        frame,
        textvariable = getStrings()["luogoEntry"]
    )

    

    genereLabel.grid(row = 0, column = 0, pady = 5, padx = 5)
    genereEntry.grid(row = 0, column = 1, pady = 5, padx = 5, sticky="nsew")
    titoloLabel.grid(row = 1, column = 0, pady = 5, padx = 5)
    titoloEntry.grid(row = 1, column = 1, pady = 5, padx = 5, sticky="nsew")
    autoreLabel.grid(row = 2, column = 0, pady = 5, padx = 5)
    autoreEntry.grid(row = 2, column = 1, pady = 5, padx = 5, sticky="nsew")
    casaeditriceLabel.grid(row = 3, column = 0, pady = 5, padx = 5)
    casaeditriceEntry.grid(row = 3, column = 1, pady = 5, padx = 5, sticky = "nsew")
    annoLabel.grid(row = 4, column = 0, pady = 5, padx = 5)
    annoEntry.grid(row = 4, column = 1, pady = 5, padx = 5, sticky="nsew")
    luogoLabel.grid(row = 5, column = 0, pady = 5, padx = 5)
    luogoEntry.grid(row = 5, column = 1, pady = 5, padx = 5, sticky="nsew")


def loadSearchButtons(frame):
    searchCloseButton = Button(
        frame,
        text = "Close",
        command = lambda: clickHandler("searchClose")
    )

    searchClearButton = Button(
        frame,
        text = "Clear",
        command = lambda: clickHandler("searchClear")
    )

    searchQueryButton = Button(
        frame,
        text = "Search",
        command = lambda: clickHandler("searchQuery")
    )

    searchCloseButton.grid(row = 0, column = 0, pady = (10, 5), padx = 5, sticky = "nsew")
    searchClearButton.grid(row = 0, column = 1, pady = (10, 5), padx = 5, sticky = "nsew")
    searchQueryButton.grid(row = 0, column = 2, pady = (10, 5), padx = 5, sticky = "nsew")


def loadBook(frame):
    getStrings()["newGenereEntry"] = StringVar(name = "newGenereEntry")
    getStrings()["newTitoloEntry"] = StringVar(name = "newTitoloEntry")
    getStrings()["newAutoreEntry"] = StringVar(name = "newAutoreEntry")
    getStrings()["newCasaeditriceEntry"] = StringVar(name = "newCasaeditriceEntry")
    getStrings()["newAnnoEntry"] = StringVar(name = "newAnnoEntry")
    getStrings()["newLuogoEntry"] = StringVar(name = "newLuogoEntry")

    genereLabel = Label(
        frame,
        text = "Genere"
    )
    genereEntry = Entry(
        frame,
        textvariable = getStrings()["newGenereEntry"]
    )

    titoloLabel = Label(
        frame,
        text = "Titolo"
    )
    titoloEntry = Entry(
        frame,
        textvariable = getStrings()["newTitoloEntry"]
    )

    autoreLabel = Label(
        frame,
        text = "Autore"
    )
    autoreEntry = Entry(
        frame,
        textvariable = getStrings()["newAutoreEntry"]
    )

    casaeditriceLabel = Label(
        frame,
        text = "Casa Editrice"
    )
    casaeditriceEntry = Entry(
        frame,
        textvariable = getStrings()["newCasaeditriceEntry"]
    )

    annoLabel = Label(
        frame,
        text = "Anno"
    )
    annoEntry = Entry(
        frame,
        textvariable = getStrings()["newAnnoEntry"]
    )

    luogoLabel = Label(
        frame,
        text = "Luogo"
    )
    luogoEntry = Entry(
        frame,
        textvariable = getStrings()["newLuogoEntry"]
    )

    

    genereLabel.grid(row = 0, column = 0, pady = 5, padx = 5)
    genereEntry.grid(row = 0, column = 1, pady = 5, padx = 5, sticky="nsew")
    titoloLabel.grid(row = 1, column = 0, pady = 5, padx = 5)
    titoloEntry.grid(row = 1, column = 1, pady = 5, padx = 5, sticky="nsew")
    autoreLabel.grid(row = 2, column = 0, pady = 5, padx = 5)
    autoreEntry.grid(row = 2, column = 1, pady = 5, padx = 5, sticky="nsew")
    casaeditriceLabel.grid(row = 3, column = 0, pady = 5, padx = 5)
    casaeditriceEntry.grid(row = 3, column = 1, pady = 5, padx = 5, sticky = "nsew")
    annoLabel.grid(row = 4, column = 0, pady = 5, padx = 5)
    annoEntry.grid(row = 4, column = 1, pady = 5, padx = 5, sticky="nsew")
    luogoLabel.grid(row = 5, column = 0, pady = 5, padx = 5)
    luogoEntry.grid(row = 5, column = 1, pady = 5, padx = 5, sticky="nsew")


def loadBookAdd(frame):
    addBookButton = Button(
        frame,
        text = "Add",
        command = lambda: clickHandler("addBookSQL")
    )

    closeBookButton = Button(
        frame,
        text = "Close",
        command = lambda: clickHandler("closeBook")
    )

    closeBookButton.grid(row = 0, column = 0, pady = (10, 5), padx = 5, sticky = "nsew")
    addBookButton.grid(row = 0, column = 1, pady = (10, 5), padx = 5, sticky = "nsew")


def loadBookModify(frame):
    modifyBookButton = Button(
        frame,
        text = "Modify",
        command = lambda: clickHandler("modifyBookSQL")
    )

    closeBookButton = Button(
        frame,
        text = "Close",
        command = lambda: clickHandler("closeBook")
    )

    closeBookButton.grid(row = 0, column = 0, pady = (10, 5), padx = 5, sticky = "nsew")
    modifyBookButton.grid(row = 0, column = 1, pady = (10, 5), padx = 5, sticky = "nsew")