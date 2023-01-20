# WIDGETS module for implementing all the widgets used in the frames

# module for styled tkinter widgets
from tkinter.ttk import *
# module for StringVar objects
from tkinter import StringVar
# module for messageboxes (errors, info)
from tkinter import messagebox
# module for all things window related
from tkinter import *
# module for creating and managing frames
from frames import *
# module for accessing global variables and construncts
from globalVars import *
# module for applying the hash function SHA256
from hashlib import sha256
# module for logging in and creating new users
from login import *
# module for creating new windows
from window import *

# dictionary of widgets to reference them after their creation
widgets = dict()

# function to handle clicks
def clickHandler(*args):
    # login behaviour
    if args[0] == "login":
        if login(getStrings()["usernameEntry"].get(), getStrings()["passwordEntry"].get()):
            # set the login flag to true
            setLogin(True)
            # set the logged in user
            setUser(getStrings()["usernameEntry"].get())
            setPassword(getStrings()["passwordEntry"].get())
            # destroy the window
            getWindow().destroy()
            # create the main app window
            createAppWindow()
            # load the frames and widgets for it
            loadWidgets(loadAppFrames())

        else:
            # notify the user that the login info is incorrect
            messagebox.showerror("Errore Login",
                                 "Username e/o Password errati")
    
    # register behaviour
    if args[0] == "register":
        # if the user doesn't provide a username
        if len(getStrings()["usernameEntry"].get()) == 0:
            # notify the user
            messagebox.showerror("Errore input",
                                 "Nome utente non presente")
            return()
        
        # if the user doesn't provide a password
        if len(getStrings()["passwordEntry"].get()) == 0:
            # notify the user
            messagebox.showerror("Errore input",
                                 "Password non presente")
            return()
        
        
        if register(getStrings()["usernameEntry"].get(), getStrings()["passwordEntry"].get()):
            # let the user know of the registration
            messagebox.showinfo("Registrazione con successo",
                                "L'utente " + getStrings()["usernameEntry"].get() + " è ora registrato")
        
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
        # get the value of the book ID from the "books" widget
        bookID = str(widgets["books"].item(widgets["books"].selection())["values"][0])
        
        # setup the query to update the value of the selected book
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
        
        # send the composed query to the database
        sendMySQL("UPDATE libri " +
                  "SET " + command +
                  "WHERE ID = '" + bookID + "';"
        )
        
        # update the book list
        clickHandler("searchQuery")

    # behaviour of the close button in the book window
    if args[0] == "closeBook":
        closeBookWindow()

    # behaviour of the reviews button in the main window
    if args[0] == "seeReviews":
        # if no book is selected
        if len(widgets["books"].selection()) == 0:
            # notify the user
            messagebox.showerror("Selection Error",
                                 "No book selected")
            return()
        
        # if the reviews window isn't already opened
        if getReviewsWindow() is None:
            # create a new reviews window
            createReviewsWindow()
            # load its widgets and frames
            loadWidgets(loadReviewsFrame())

    # behaviour of the borrow button in the main window
    if args[0] == "borrow":
        # if there is no book selected
        if len(widgets["books"].selection()) == 0:
            # notify the user
            messagebox.showerror("Errore di selezione",
                                 "Non è stato selezionato nessun libro")
            return()

        # hashed password to check if it matches in the database
        hashedPassword = sha256(getPassword().encode('utf-8')).hexdigest()
        # string containing the selected book ID
        selectedBook = str(widgets["books"].item(widgets["books"].selection())["values"][0])
        
        # query to get the book owned by the current user
        ownedBook = sendMySQL("SELECT IDLibro " +
                              "FROM utenti " +
                              "WHERE Nome = '" + getUser() + "' "
                              "AND Password = '" + hashedPassword + "';")
        
        # if the user already owns a book
        if not(ownedBook[0][0] is None):
            # notify the user
            messagebox.showerror("Errore di prestito",
                                 "Possiedi già un libro in prestito")
            return()
        
        # query to check if the selected book is already owened by another user
        availability = sendMySQL("SELECT IDLibro " +
                                 "FROM utenti " +
                                 "WHERE IDLibro = '" + selectedBook + "';")
        
        # if the book is already borrowed
        if len(availability) != 0:
            # notify the user
            messagebox.showerror("Errore di selezione",
                                 "Questo libro è già stato preso in prestito")
            return()
        
        # query to update  the user's owned book ID with the selected one
        sendMySQL("UPDATE utenti " +
                  "SET IDLibro = '" + selectedBook + "' " +
                  "WHERE Nome = '" + getUser() + "' " +
                  "AND Password = '" + hashedPassword + "';")
        
        # update the UI to show the owned book
        setBooksOwned(widgets["books"].item(widgets["books"].selection())["values"][2])
        getStrings()["booksOwned"].set("Libro: " + widgets["books"].item(widgets["books"].selection())["values"][2])
        
    # behaviour of the return button in the main window
    if args[0] == "return":
        # if the user doesn't own any book
        if getBooksOwned() == "":
            # notify the user
            messagebox.showerror("Errore",
                                 "Non possiedi nessun libro")
            return()
        
        # if the return window isn't open yet
        if getReturnWindow() is None:
            # create a new return window
            createReturnWindow()
            # load its widgets and frames
            loadWidgets(loadReturnFrame())
            
    # behaviour of the close button in the return window
    if args[0] == "closeReturn":
        closeReturnWindow()
        
    # behaviour of the return button in the return window   
    if args[0] == "returnButton":
        # hash the password to check the matching on the database
        hashedPassword = sha256(getPassword().encode('utf-8')).hexdigest()
        # get the ID of the book owned by the current user
        ownedBook = sendMySQL("SELECT IDLibro " +
                              "FROM utenti " +
                              "WHERE Nome = '" + getUser() + "' "
                              "AND Password = '" + hashedPassword + "';")
        # if the value is None (NULL)
        if ownedBook[0][0] is None:
            # notify the user that they don't have any book owned
            messagebox.showerror("Errore Restituzione",
                                 "Non possiedi alcun libro da restituire")
            return()
        
        # if the length of the comment is too large
        if len(widgets["commentTextBox"].get(1.0, "end-1c")) > 1023:
            # notify the user
            messagebox.showerror("Errore di commento",
                                 "Il commento non può superare i 1023 caratteri")
            return()
        
        
        # get the previews review left by the current user on the current book
        previousReview = sendMySQL("SELECT * " + 
                                   "FROM restituzioni " + 
                                   "WHERE Nome = '" + getUser() + "' " +
                                   "AND Password = '" + hashedPassword + "' "
                                   "AND IDLibro = '" + str(ownedBook[0][0]) + "';")
        
        # if there is no previous review left, create a new one
        if len(previousReview) == 0:
            # default construction of the INSERT query to return the book
            insertSQL = "INSERT INTO restituzioni(Nome, Password, IDLibro, Voto"
            valuesSQL = "VALUES ('" + getUser() + "', '" + hashedPassword + "', '" + str(ownedBook[0][0]) + "', '" + getStrings()["scoreDropdown"].get() + "'"
            
            # if the user left a comment, add it in the query
            if widgets["commentTextBox"].get(1.0, "end-1c") != "":
                insertSQL += ", Commento) "
                valuesSQL += ", '" + widgets["commentTextBox"].get(1.0, "end-1c") + "');"
            # otherwise terminate the query as it is
            else:
                insertSQL += ") "
                valuesSQL += ");"
            
            # send the query to return the book in the "restituzioni" table
            sendMySQL(insertSQL + valuesSQL)
            
        # otherwise if a review already exists, update the existing one
        else:
            # default construction of the UPDATE query to leave a review
            updateSQL = "UPDATE restituzioni SET Voto = '" + getStrings()["scoreDropdown"].get() + "'"
            whereSQL = "WHERE Nome = '" + getUser() + "' AND Password = '" + hashedPassword + "';"
            
            # if the user left a comment, add it in the query
            if widgets["commentTextBox"].get(1.0, "end-1c") != "":
                updateSQL += ", Commento = '" + widgets["commentTextBox"].get(1.0, "end-1c") + "' "
            else:
                updateSQL += ", Commento = NULL "
            
            # send the query
            sendMySQL(updateSQL + whereSQL)
        
        # update the user's owned book in the "utenti" table
        sendMySQL("UPDATE utenti " +
                  "SET IDLibro = NULL " +
                  "WHERE Nome = '" + getUser() + "' " +
                  "AND Password = '" + hashedPassword + "';")
        
        # update the UI to show the owned book
        getStrings()["booksOwned"].set("Libro: ")
        setBooksOwned("")


# function to load widgets into the respective frames
def loadWidgets(frames):
    # login frame
    if "loginF" in frames:
        loadLogin(frames["loginF"])
    # app user info frame (NW)
    if "appFUserInfo" in frames:
        loadAppUserInfo(frames["appFUserInfo"])
    # app manage books frame (NC)
    if "appFManageBook" in frames:
        loadAppManageBook(frames["appFManageBook"])
    # app search frame (NE)
    if "appFSearch" in frames:
        loadAppSearch(frames["appFSearch"])
    # app database frame (CW)
    if "appFDatabase" in frames:
        loadAppDatabase(frames["appFDatabase"])
    # app logout frame (SW)
    if "appFLogout" in frames:
        loadAppLogout(frames["appFLogout"])
    # app review frame (SC)
    if "appFReview" in frames:
        loadAppReview(frames["appFReview"])
    # app modify library frame (SE)
    if "appFModifyLibrary" in frames:
        loadAppModifyLibrary(frames["appFModifyLibrary"])
    # search frame
    if "searchFrame" in frames:
        loadSearch(frames["searchFrame"])
    # search buttons frame
    if "searchButtonsFrame" in frames:
        loadSearchButtons(frames["searchButtonsFrame"])
    # book frame
    if "bookFrame" in frames:
        loadBook(frames["bookFrame"])
    # book buttons (add) frame
    if "bookAddFrame" in frames:
        loadBookAdd(frames["bookAddFrame"])
    # book buttons (modify) frame
    if "bookModifyFrame" in frames:
        loadBookModify(frames["bookModifyFrame"])
    # reviews frame
    if "reviewsFrame" in frames:
        loadReviews(frames["reviewsFrame"])
    # return frame
    if "returnFrame" in frames:
        loadReturn(frames["returnFrame"])



# FUNCTIONS TO LOAD WIDGETS TO FRAMES

# LOGIN WINDOW
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

# MAIN APP WINDOW
# function to load the user info frame widgets (NW)
def loadAppUserInfo(frame):
    # create a new StringVar for the owned book
    getStrings()["booksOwned"] = StringVar(name = "booksOwned")
    # set it as "Libro: " + the owned book by the user
    getStrings()["booksOwned"].set("Libro: " + str(getBooksOwned()))

    # label for the username
    userLabel = Label(
        frame,
        text = "User: " + getUser(),
    )

    # label for the owned book
    booksLabel = Label(
        frame,
        textvariable = getStrings()["booksOwned"]
    )

    # pack the widgets in the frame
    userLabel.pack(pady = (10, 0), padx = (10, 0), anchor = W)
    booksLabel.pack(pady = (0, 10), padx = (10, 0), anchor = W)

    # store the books label widget in the dictionary
    widgets["booksLabel"] = booksLabel

# function to load the book management frame widgets (NC)
def loadAppManageBook(frame):
    # borrow button to borrow a book
    borrowButton = Button(
        frame,
        text = "Prendi in prestito",
        command = lambda: clickHandler("borrow")
    )
    
    # return button to open the return window
    returnButton = Button(
        frame,
        text = "Restituisci Libro",
        command = lambda: clickHandler("return")
    )
    
    # pack the widgets to the frame
    borrowButton.pack(side = LEFT, padx = 10, pady = 15)
    returnButton.pack(side = LEFT, padx = 10, pady = 15)

# function to load the search frame widgets in the app window (NE)
def loadAppSearch(frame):
    # button to open the search window
    searchButton = Button(
        frame,
        text = "Search",
        command = lambda: clickHandler("search")
    )

    # pack the widget to the frame
    searchButton.pack(side = RIGHT, padx = 10, pady = 15)

# function to laod the database frame widgets (CW)
def loadAppDatabase(frame):
    # make a query to check all the books in the database
    result = sendMySQL("SELECT * FROM libri;")

    # setup the columns with all the attributes in the books table
    columns = ('id', 'genere', 'titolo', 'autore', 'casaeditrice', 'anno', 'luogo')

    # tree view widget to display the books
    books = Treeview(
        frame,
        columns = columns,
        show = 'headings'
    )

    # setup the heading names for the visible attributes
    books.heading('genere', text="Genere")
    books.heading('titolo', text="Titolo")
    books.heading('autore', text="Autore")
    books.heading('casaeditrice', text="Casa Editrice")
    books.heading('anno', text="Anno")
    books.heading('luogo', text="Luogo")

    # if the query returned any value, store it in the widget
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

    # create a scrollbar to scroll through the books and bind it to the widget
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=books.yview)
    books.configure(yscroll=scrollbar.set)
    
    # make the ID column invisible to the user
    books["displaycolumns"] = ('genere', 'titolo', 'autore', 'casaeditrice', 'anno', 'luogo')
    
    # pack the treeview and scrollbar widgets to the frame
    books.pack(expand = True, fill = "both", side = LEFT)
    scrollbar.pack(side = LEFT, fill = Y)
    
    # store the books widget to the dictionary
    widgets["books"] = books

# function to load the logout frame widgets (SW)
def loadAppLogout(frame):
    # button to close the program
    closeButton = Button(
        frame,
        text = "Close",
        command = lambda: clickHandler("close")
    )
    # button to logout from the current user
    logoutButton = Button(
        frame,
        text = "Logout",
        command = lambda: clickHandler("logout")
    )

    # pack the widgets to the frame
    closeButton.pack(padx = 10, pady = 10, side = LEFT)
    logoutButton.pack(padx = 10, pady = 10, side = LEFT)

# function to load the reviews frame widgets in the main window (SC)
def loadAppReview(frame):
    # button to open the reviews window
    reviewButton = Button(
        frame,
        text = "See Reviews",
        command = lambda: clickHandler("seeReviews")
    )
    
    # pack the widget to the frame
    reviewButton.pack(padx = 10, pady = 10)

# function to load the modify library frame widgets in the main window (SE)
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


# SEARCH WINDOW
# function to load the search frame widgets
def loadSearch(frame):
    # if there wasn't any previous entry input by the user, create new StringVar objects for each parameter of the search
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

    # label for the genre
    genereLabel = Label(
        frame,
        text = "Genere"
    )
    # entry for the genre
    genereEntry = Entry(
        frame,
        textvariable = getStrings()["genereEntry"]
    )

    # label for the title
    titoloLabel = Label(
        frame,
        text = "Titolo"
    )
    # entry for the title
    titoloEntry = Entry(
        frame,
        textvariable = getStrings()["titoloEntry"]
    )

    # label for the author
    autoreLabel = Label(
        frame,
        text = "Autore"
    )
    # entry for the author
    autoreEntry = Entry(
        frame,
        textvariable = getStrings()["autoreEntry"]
    )

    # lable for the publisher
    casaeditriceLabel = Label(
        frame,
        text = "Casa Editrice"
    )
    # entry for the publisher
    casaeditriceEntry = Entry(
        frame,
        textvariable = getStrings()["casaeditriceEntry"]
    )

    # label for the year
    annoLabel = Label(
        frame,
        text = "Anno"
    )
    # entry for the year
    annoEntry = Entry(
        frame,
        textvariable = getStrings()["annoEntry"]
    )

    # label for the place
    luogoLabel = Label(
        frame,
        text = "Luogo"
    )
    # entry for the place
    luogoEntry = Entry(
        frame,
        textvariable = getStrings()["luogoEntry"]
    )

    # place the widgets in the frame
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

# function to laod the search buttons frame widgets
def loadSearchButtons(frame):
    # button for closing the search window
    searchCloseButton = Button(
        frame,
        text = "Close",
        command = lambda: clickHandler("searchClose")
    )
    # button for clearing the search entries
    searchClearButton = Button(
        frame,
        text = "Clear",
        command = lambda: clickHandler("searchClear")
    )
    # button for searching according to the user input
    searchQueryButton = Button(
        frame,
        text = "Search",
        command = lambda: clickHandler("searchQuery")
    )

    # place the widgets in the frame
    searchCloseButton.grid(row = 0, column = 0, pady = (10, 5), padx = 5, sticky = "nsew")
    searchClearButton.grid(row = 0, column = 1, pady = (10, 5), padx = 5, sticky = "nsew")
    searchQueryButton.grid(row = 0, column = 2, pady = (10, 5), padx = 5, sticky = "nsew")


# BOOK WINDOW
# function to load the book frame widgets
def loadBook(frame):
    # create new stringVar objects for the entries of the window
    getStrings()["newGenereEntry"] = StringVar(name = "newGenereEntry")
    getStrings()["newTitoloEntry"] = StringVar(name = "newTitoloEntry")
    getStrings()["newAutoreEntry"] = StringVar(name = "newAutoreEntry")
    getStrings()["newCasaeditriceEntry"] = StringVar(name = "newCasaeditriceEntry")
    getStrings()["newAnnoEntry"] = StringVar(name = "newAnnoEntry")
    getStrings()["newLuogoEntry"] = StringVar(name = "newLuogoEntry")

    # label for the genre
    genereLabel = Label(
        frame,
        text = "Genere"
    )
    # entry for the genre
    genereEntry = Entry(
        frame,
        textvariable = getStrings()["newGenereEntry"]
    )
    # label for the title
    titoloLabel = Label(
        frame,
        text = "Titolo"
    )
    # entry for the title
    titoloEntry = Entry(
        frame,
        textvariable = getStrings()["newTitoloEntry"]
    )
    # label for the author
    autoreLabel = Label(
        frame,
        text = "Autore"
    )
    # entry for the author
    autoreEntry = Entry(
        frame,
        textvariable = getStrings()["newAutoreEntry"]
    )
    # label for the publisher
    casaeditriceLabel = Label(
        frame,
        text = "Casa Editrice"
    )
    # entry for the publisher
    casaeditriceEntry = Entry(
        frame,
        textvariable = getStrings()["newCasaeditriceEntry"]
    )
    # label for the year
    annoLabel = Label(
        frame,
        text = "Anno"
    )
    # entry for the year
    annoEntry = Entry(
        frame,
        textvariable = getStrings()["newAnnoEntry"]
    )
    # label for the place
    luogoLabel = Label(
        frame,
        text = "Luogo"
    )
    # entry for the place
    luogoEntry = Entry(
        frame,
        textvariable = getStrings()["newLuogoEntry"]
    )

    # place the widgts in the frame
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

# function to load the book add buttons frame widgets
def loadBookAdd(frame):
    # button to add a new book
    addBookButton = Button(
        frame,
        text = "Add",
        command = lambda: clickHandler("addBookSQL")
    )
    # button to close the book window
    closeBookButton = Button(
        frame,
        text = "Close",
        command = lambda: clickHandler("closeBook")
    )

    # place the widgets in the frame
    closeBookButton.grid(row = 0, column = 0, pady = (10, 5), padx = 5, sticky = "nsew")
    addBookButton.grid(row = 0, column = 1, pady = (10, 5), padx = 5, sticky = "nsew")

# function to load the book modify buttons frame widgets
def loadBookModify(frame):
    # button to modify the selected book with the entries provided by the user
    modifyBookButton = Button(
        frame,
        text = "Modify",
        command = lambda: clickHandler("modifyBookSQL")
    )
    # button to close the book window
    closeBookButton = Button(
        frame,
        text = "Close",
        command = lambda: clickHandler("closeBook")
    )

    # place the widgets in the frame
    closeBookButton.grid(row = 0, column = 0, pady = (10, 5), padx = 5, sticky = "nsew")
    modifyBookButton.grid(row = 0, column = 1, pady = (10, 5), padx = 5, sticky = "nsew")
    

# REVIEWS WINDOW
# function to load the reviews frame widgets 
def loadReviews(frame):
    # create a temporary frame for the treeview
    treeFrame = Frame(frame)
    # place the temporary frame on the frame
    treeFrame.grid(column = 0, row = 1, sticky = "nsew") 
    
    # get the ID of the selected book
    selectedBook = str(widgets["books"].item(widgets["books"].selection())["values"][0])
    
    # get the average score of the selected book
    averageScoreDatabase = sendMySQL("SELECT AVG(Voto) FROM restituzioni WHERE IDLibro = '" + selectedBook + "';")

    # label for the average score
    averageScore = Label(
        frame,
        text = "Voto medio: " + str(averageScoreDatabase[0][0])
    )
    
    # get the score and comment of all the reviews of the selected book
    reviewsDatabase = sendMySQL("SELECT Voto, Commento FROM restituzioni WHERE IDLibro = '" + selectedBook + "';")

    # setup the columns of the treeview
    columns = ('voto', 'commento')
    # treeview to display the score and comment of the reviews
    reviews = Treeview(
        treeFrame,
        columns = columns,
        show = 'headings'
    )
    # setup the name of the columns in the treeview
    reviews.heading('voto', text="Voto (0 - 5)")
    reviews.heading('commento', text="Commento")

    # fill the treeview with the values from the query
    if reviewsDatabase != None:
        for i in range(len(reviewsDatabase)):
            reviews.insert('', END, values = (
                reviewsDatabase[i][0],
                reviewsDatabase[i][1],
            ))

    # change the width of the score column
    reviews.column("voto", width = 20)

    # add a scrollbar to the treeview
    scrollbar = Scrollbar(treeFrame, orient=VERTICAL, command=reviews.yview)
    reviews.configure(yscroll=scrollbar.set)   
    
    # place the widgets in the frames
    averageScore.grid(column = 0, row = 0, pady = 5)
    reviews.pack(expand = True, fill = "both", side = LEFT)
    scrollbar.pack(side = LEFT, fill = Y)
    

# RETURN WINDOW
# function to load the widgets for the return frame
def loadReturn(frame):
    # create a new StringVar object for the dropdown for the score
    getStrings()["scoreDropdown"] = StringVar(name = "scoreDropdown")
    getStrings()["scoreDropdown"].set("5")
    
    # label for the selected book
    returningBookLabel = Label(
        frame,
        text = getBooksOwned()
    )
    
    # label for the score
    scoreLabel = Label(
        frame,
        text = "Voto"
    )
    
    # dropdown menue for the score
    options = ["0", "1", "2", "3", "4", "5"]
    scoreDropdown = OptionMenu(
        frame,
        getStrings()["scoreDropdown"],
        *options
    )
    
    # label for the comment
    commentLabel = Label(
        frame,
        text = "Commento"
    )
    # text area to write a comment
    commentTextBox = Text(
        frame,
        height = 5,
        width = 20
    )
    
    # button to close the return window
    returnCloseButton = Button(
        frame,
        text = "Chiudi",
        command = lambda: clickHandler("closeReturn")
    )
    # button to return the book and leave the review from the user
    returnButton = Button(
        frame,
        text = "Restituisci",
        command = lambda: clickHandler("returnButton")
    )
    
    # place the widgets in the frame
    returningBookLabel.grid(column = 0, row = 0, columnspan = 2, padx = 10)
    scoreLabel.grid(column = 0, row = 1, columnspan = 2, padx = 10, sticky = "s")
    scoreDropdown.grid(column = 0, row = 2, columnspan = 2, padx = 10)
    commentLabel.grid(column = 0, row = 3, columnspan = 2, padx = 10, sticky = "s")
    commentTextBox.grid(column = 0, row = 4, columnspan = 2, padx = 10, sticky = "ew")
    returnCloseButton.grid(column = 0, row = 5, padx = 10, sticky = "e")
    returnButton.grid(column = 1, row = 5, columnspan = 2, padx = 10, sticky = "w")
    
    # store the comment textbox widget in the dictionary
    widgets["commentTextBox"] = commentTextBox