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

# dictionary of widgets to reference them after their creation
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
            setPassword(getStrings()["passwordEntry"].get())
            # destroy the window (replace with function)
            getWindow().destroy()
            
            createAppWindow()
            loadWidgets(loadAppFrames())

        else:
            # notify the user that the login info is incorrect
            messagebox.showerror("Errore Login",
                                 "Username e/o Password errati")
    
    # register behaviour
    if args[0] == "register":
        if register(getStrings()["usernameEntry"].get(), getStrings()["passwordEntry"].get()):
            # let the user know of the registration
            messagebox.showinfo("Registrazione con successo",
                                "L'utente " +
                                getStrings()["usernameEntry"].get() +
                                " è ora registrato")
        
        else:
            # notify the user that the username already exists
            messagebox.showerror("Errore Registrazione",
                                 "Utente già esistente")

    # logout behaviour
    if args[0] == "logout":
        # set the login flag to false
        setLogin(False)
        # reset the logged in user value
        setUser("")

        # close all the pop-up windows
        if getSearchWindow() != None:
            closeSearchWindow()
        if getBookWindow() != None:
            closeBookWindow()
        if getReviewsWindow() != None:
            closeReviewsWindow()
        if getReturnWindow() != None:
            closeReturnWindow()

        # close the main app window
        getWindow().destroy()
        
        # create a new login window
        createLoginWindow()
        # load its widgets
        loadWidgets(loadLoginFrames())
        
    # close behaviour   
    if args[0] == "close":
        # close the main window
        getWindow().destroy()

    # behaviour of the search button
    if args[0] == "search":
        # if the search window isn't already opened
        if getSearchWindow() is None:
            # create the search window
            createSearchWindow()
            # load its widgets
            loadWidgets(loadSearchFrames())

    # behaviour of the search button in the search window            
    if args[0] == "searchQuery":
        # delete the existing entries in the books list
        children = widgets["books"].get_children()
        for child in children:
            widgets["books"].delete(child)

        # setup the query (attributes are searched with the LIKE %*attribute*% format)
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
        # send the query to the database
        result = sendMySQL(query)

        # update the books widget with the new results from the search query
        for i in range(len(result)):
            widgets["books"].insert('', END, values = (
                result[i][0],
                result[i][1],
                result[i][2],
                result[i][3],
                result[i][4],
                result[i][5],
                result[i][6],
            ))

    # behaviour of the close button in the search window
    if args[0] == "searchClose":
        # close the search window
        closeSearchWindow()

    # behaviour of the clear button in the search window
    if args[0] == "searchClear":
        # reset the stringvar values for each entry of the search
        getStrings()["genereEntry"].set("")
        getStrings()["titoloEntry"].set("")
        getStrings()["autoreEntry"].set("")
        getStrings()["casaeditriceEntry"].set("")
        getStrings()["annoEntry"].set("")
        getStrings()["luogoEntry"].set("")

    # behaviour of the add book button
    if args[0] == "addBook":
        # if the book window isn't already opened
        if getBookWindow() is None:
            # create a book window
            createBookWindow()
            # load its widgets (with the add parameter)
            loadWidgets(loadBookFrames("add"))
    
    # behaviour of the modify book button
    if args[0] == "modifyBook":
        # if no book is selected
        if len(widgets["books"].selection()) == 0:
            # notify the error to the user
            messagebox.showerror("Selection Error",
                                 "No book selected")
            return()

        # if the book window isn't already opened
        if getBookWindow() is None:
            # create a book window
            createBookWindow()
            # load its widgets (with the modify parameter)
            loadWidgets(loadBookFrames("modify"))

            # get the selected book
            item = widgets["books"].item(widgets["books"].selection()[0])
            values = item['values']
            
            # set the stringvar for the entries in the window to the selected book values
            getStrings()["newGenereEntry"].set(values[1])
            getStrings()["newTitoloEntry"].set(values[2])
            getStrings()["newAutoreEntry"].set(values[3])
            getStrings()["newCasaeditriceEntry"].set(values[4])
            getStrings()["newAnnoEntry"].set(values[5])
            getStrings()["newLuogoEntry"].set(values[6])

    # behaviour of the remove book button
    if args[0] == "removeBook":
        # if no book is selected
        if len(widgets["books"].selection()) == 0:
            # notify the user of the error
            messagebox.showerror("Selection Error",
                                 "No book selected")
            return()

        # for each book selected
        for selected_item in widgets["books"].selection():
            item = widgets["books"].item(selected_item)
            values = item['values']
            # delete the entry from the database
            sendMySQL("DELETE FROM libri " +
                      "WHERE ID = '" + str(values[0]) + "';")

        # update the view of the books by making a new search query
        clickHandler("searchQuery")          

    # behaviour of the add book button in the book window
    if args[0] == "addBookSQL":
        columns = []
        values = []

        # store the values of all the entries provided by the user
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

        # if the user didn't provide a single entry for the new book
        if len(columns) == 0:
            # notify the user of the error
            messagebox.showerror("Errore di inserimento",
                                 "Non è stata fornita nessuna informazioni sul libro")
            return()

        # compose the query depending on the information provided
        tableColumns = ""
        tableValues = ""

        for i in range(len(columns)):
            tableColumns += columns[i]
            tableValues += "'" + values[i] + "'"

            if i != len(columns) - 1:
                tableColumns += ", "
                tableValues += ", "
                
        # send the query to the database
        sendMySQL("INSERT INTO libri(" + tableColumns + ") " +
                  "VALUES (" + tableValues + ");")

        # update the view of the books by making a new search query
        clickHandler("searchQuery")

    # behaviour of the modify book button in the book window
    if args[0] == "modifyBookSQL":
        bookID = str(widgets["books"].item(widgets["books"].selection())["values"][0])
        
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
                  "WHERE ID = '" + bookID + "';"
        )
        
        clickHandler("searchQuery")


    if args[0] == "closeBook":
        closeBookWindow()


    if args[0] == "seeReviews":
        if len(widgets["books"].selection()) == 0:
            messagebox.showerror("Selection Error",
                                 "No book selected")
            return()
        
        if getReviewsWindow() is None:
            createReviewsWindow()
            loadWidgets(loadReviewsFrame())


    if args[0] == "borrow":
        if len(widgets["books"].selection()) == 0:
            messagebox.showerror("Selection Error",
                                 "No book selected")
            return()

        hashedPassword = sha256(getPassword().encode('utf-8')).hexdigest()
        selectedBook = str(widgets["books"].item(widgets["books"].selection())["values"][0])
        
        ownedBook = sendMySQL("SELECT IDLibro " +
                              "FROM utenti " +
                              "WHERE Nome = '" + getUser() + "' "
                              "AND Password = '" + hashedPassword + "';")
        
        if not(ownedBook[0][0] is None):
            messagebox.showerror("Borrow Error",
                                 "You already have a book borrowed")
            return()
        
        
        availability = sendMySQL("SELECT IDLibro " +
                                 "FROM utenti " +
                                 "WHERE IDLibro = '" + selectedBook + "';")
        
        if len(availability) != 0:
            messagebox.showerror("Selection Error",
                                 "Book has been already borrowed")
            return()
        
        
        sendMySQL("UPDATE utenti " +
                  "SET IDLibro = '" + selectedBook + "' " +
                  "WHERE Nome = '" + getUser() + "' " +
                  "AND Password = '" + hashedPassword + "';")
        
        setBooksOwned(widgets["books"].item(widgets["books"].selection())["values"][2])
        
        getStrings()["booksOwned"].set("Libro: " + widgets["books"].item(widgets["books"].selection())["values"][2])
        

    if args[0] == "return":
        if getBooksOwned() == "":
            messagebox.showerror("Errore",
                                 "Non possiedi nessun libro")
            return()
        
        if getReturnWindow() is None:
            createReturnWindow()
            loadWidgets(loadReturnFrame())
            
    
    if args[0] == "closeReturn":
        closeReturnWindow()
        
    
    if args[0] == "returnButton":
        hashedPassword = sha256(getPassword().encode('utf-8')).hexdigest()
        
        ownedBook = sendMySQL("SELECT IDLibro " +
                              "FROM utenti " +
                              "WHERE Nome = '" + getUser() + "' "
                              "AND Password = '" + hashedPassword + "';")
        
        if ownedBook[0][0] is None:
            messagebox.showerror("Return Error",
                                 "You don't have any book to return")
            return()
        
        if len(widgets["commentTextBox"].get(1.0, "end-1c")) > 1023:
            messagebox.showerror("Comment Error",
                                 "Comment cannot be longer than 1024 characters")
            return()
        
        insertSQL = "INSERT INTO restituzioni(Nome, Password, IDLibro, Voto"
        valuesSQL = "VALUES ('" + getUser() + "', '" + hashedPassword + "', '" + str(ownedBook[0][0]) + "', '" + getStrings()["scoreDropdown"].get() + "'"
        
        if widgets["commentTextBox"].get(1.0, "end-1c") != "":
            insertSQL += ", Commento) "
            valuesSQL += ", '" + widgets["commentTextBox"].get(1.0, "end-1c") + "');"
            
        else:
            insertSQL += ") "
            valuesSQL += ");"
            
        sendMySQL(insertSQL + valuesSQL)
        
        sendMySQL("UPDATE utenti " +
                  "SET IDLibro = NULL " +
                  "WHERE Nome = '" + getUser() + "' " +
                  "AND Password = '" + hashedPassword + "';")
        
        getStrings()["booksOwned"].set("Libro: ")
        setBooksOwned("")
            


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
    
    if "appFManageBook" in frames:
        loadAppManageBook(frames["appFManageBook"])
    
    if "appFSearch" in frames:
        loadAppSearch(frames["appFSearch"])
    
    if "appFDatabase" in frames:
        loadAppDatabase(frames["appFDatabase"])

    if "appFLogout" in frames:
        loadAppLogout(frames["appFLogout"])

    if "appFReview" in frames:
        loadAppReview(frames["appFReview"])
        
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
        
    if "reviewsFrame" in frames:
        loadReviews(frames["reviewsFrame"])
        
    if "returnFrame" in frames:
        loadReturn(frames["returnFrame"])

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
    getStrings()["booksOwned"].set("Libro: " + str(getBooksOwned()))

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

    widgets["booksLabel"] = booksLabel


def loadAppManageBook(frame):
    borrowButton = Button(
        frame,
        text = "Prendi in prestito",
        command = lambda: clickHandler("borrow")
    )
    
    returnButton = Button(
        frame,
        text = "Restituisci Libro",
        command = lambda: clickHandler("return")
    )
    
    
    borrowButton.pack(side = LEFT, padx = 10, pady = 15)
    returnButton.pack(side = LEFT, padx = 10, pady = 15)


def loadAppSearch(frame):
    searchButton = Button(
        frame,
        text = "Search",
        command = lambda: clickHandler("search")
    )

    searchButton.pack(side = RIGHT, padx = 10, pady = 15)


def loadAppDatabase(frame):
    result = sendMySQL("SELECT * FROM libri;")

    columns = ('id', 'genere', 'titolo', 'autore', 'casaeditrice', 'anno', 'luogo')

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
                result[i][6],
            ))

    scrollbar = Scrollbar(frame, orient=VERTICAL, command=books.yview)
    books.configure(yscroll=scrollbar.set)
    books["displaycolumns"] = ('genere', 'titolo', 'autore', 'casaeditrice', 'anno', 'luogo')

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


def loadAppReview(frame):
    reviewButton = Button(
        frame,
        text = "See Reviews",
        command = lambda: clickHandler("seeReviews")
    )
    
    reviewButton.pack(padx = 10, pady = 10)



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
    
    
def loadReviews(frame):
    treeFrame = Frame(frame)
    treeFrame.grid(column = 0, row = 1, sticky = "nsew") 
    
    selectedBook = str(widgets["books"].item(widgets["books"].selection())["values"][0])
    
    averageScoreDatabase = sendMySQL("SELECT AVG(Voto) FROM restituzioni WHERE IDLibro = '" + selectedBook + "';")

    averageScore = Label(
        frame,
        text = "Voto medio: " + str(averageScoreDatabase[0][0])
    )
    
    
    reviewsDatabase = sendMySQL("SELECT Voto, Commento FROM restituzioni WHERE IDLibro = '" + selectedBook + "';")

    columns = ('voto', 'commento')

    reviews = Treeview(
        treeFrame,
        columns = columns,
        show = 'headings'
    )

    reviews.heading('voto', text="Voto (0 - 5)")
    reviews.heading('commento', text="Commento")

    if reviewsDatabase != None:
        for i in range(len(reviewsDatabase)):
            reviews.insert('', END, values = (
                reviewsDatabase[i][0],
                reviewsDatabase[i][1],
            ))

    reviews.column("voto", width = 20)

    scrollbar = Scrollbar(treeFrame, orient=VERTICAL, command=reviews.yview)
    reviews.configure(yscroll=scrollbar.set)   
    
    averageScore.grid(column = 0, row = 0, pady = 5)
    
    reviews.pack(expand = True, fill = "both", side = LEFT)
    scrollbar.pack(side = LEFT, fill = Y)
    

def loadReturn(frame):
    getStrings()["scoreDropdown"] = StringVar(name = "scoreDropdown")
    getStrings()["scoreDropdown"].set("5")
    
    returningBookLabel = Label(
        frame,
        text = "INSERT BOOK"
    )
    
    scoreLabel = Label(
        frame,
        text = "Voto"
    )
    
    options = ["0", "1", "2", "3", "4", "5"]
    
    scoreDropdown = OptionMenu(
        frame,
        getStrings()["scoreDropdown"],
        *options
    )
    
    
    commentLabel = Label(
        frame,
        text = "Commento"
    )
    
    commentTextBox = Text(
        frame,
        height = 5,
        width = 20
    )
    
    
    returnCloseButton = Button(
        frame,
        text = "Chiudi",
        command = lambda: clickHandler("closeReturn")
    )
    
    returnButton = Button(
        frame,
        text = "Restituisci",
        command = lambda: clickHandler("returnButton")
    )
    
    
    returningBookLabel.grid(column = 0, row = 0, columnspan = 2, padx = 10)
    scoreLabel.grid(column = 0, row = 1, columnspan = 2, padx = 10, sticky = "s")
    scoreDropdown.grid(column = 0, row = 2, columnspan = 2, padx = 10)
    commentLabel.grid(column = 0, row = 3, columnspan = 2, padx = 10, sticky = "s")
    commentTextBox.grid(column = 0, row = 4, columnspan = 2, padx = 10, sticky = "ew")
    returnCloseButton.grid(column = 0, row = 5, padx = 10, sticky = "e")
    returnButton.grid(column = 1, row = 5, columnspan = 2, padx = 10, sticky = "w")
    
    widgets["commentTextBox"] = commentTextBox