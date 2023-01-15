import mysql.connector

# window object
window = None
# search window
searchWindow = None
# book window
bookWindow = None

# flag to keep track of the login
loggedIn = True # MOCK DATA
# flag to keep track of the program execution
running = True
# string for the logged in user
user = "joshua" # MOCK DATA

booksOwned = 20 # MOCK DATA

strings = dict()

ints = dict()

mydb = None

try:
    # MySQL database connection
    mydb = mysql.connector.connect(
                host = "192.168.0.105",
                user = "josh",
                password = "password",
                database = "biblioteca"
            )
    # cursor to issue commands to the database
    cursor = mydb.cursor(buffered = True)

except Exception as e:
    print(e)


# function to send commands to the database
def sendMySQL(command):
    global mydb

    result = None

    try:
        # send the MySQL command
        cursor.execute(command)
        print(cursor)
        # store the result
        result = cursor.fetchall()
        # commit the changes to the database
        mydb.commit()
    
    except Exception as e:
        print(e)

    finally:
        # return the result of the command
        return(result)


def closeProgram():
    global running
    global window

    running = False
    window.destroy()

# SETTERS AND GETTERS FOR GLOBAL VARIABLES
def getWindow():
    global window
    return(window)

def setWindow(newWindow):
    global window
    window = newWindow



def getSearchWindow():
    global searchWindow
    return(searchWindow)

def setSearchWindow(newWindow):
    global searchWindow
    searchWindow = newWindow

def closeSearchWindow():
    global searchWindow
    searchWindow.destroy()
    searchWindow = None


def getBookWindow():
    global bookWindow
    return(bookWindow)

def setBookWindow(newWindow):
    global bookWindow
    bookWindow = newWindow

def closeBookWindow():
    global bookWindow
    bookWindow.destroy()
    bookWindow = None


def checkLoggedIn():
    global loggedIn
    print(loggedIn)

def setLogin(flag):
    global loggedIn
    loggedIn = flag

def getLogin():
    global loggedIn
    return(loggedIn)


def checkUser():
    global user
    print(user)

def setUser(newUser):
    global user
    user = newUser

def getUser():
    global user
    return(user)


def setBooksOwned(newBooks):
    global booksOwned
    booksOwned = newBooks

def getBooksOwned():
    global booksOwned
    return(booksOwned)


def getStrings():
    global strings
    return(strings)

def setStrings(newStrings):
    global strings
    strings = newStrings


def getInts():
    global ints
    return(ints)

def getRunning():
    global running
    return(running)

def setRunning(newRunning):
    global running
    running = newRunning