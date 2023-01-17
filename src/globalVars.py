import mysql.connector

# window object
window = None
# search window
searchWindow = None
# book window
bookWindow = None
# reviews window
reviewsWindow = None
# return window
returnWindow = None


# flag to keep track of the login
loggedIn = False # MOCK DATA
# flag to keep track of the program execution
running = True
# string for the logged in user
user = "joshua" # MOCK DATA
password = ""

booksOwned = "" # MOCK DATA

strings = dict()

ints = dict()

mydb = None

try:
    # MySQL database connection
    mydb = mysql.connector.connect(
                host = "solidgallium.ddns.net",
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


def callSQLProcedure(procedure, params):
    global mydb
    
    result = None
    
    try:
        cursor.callproc(procedure, params)
        print(cursor)
        result = cursor.stored_results()
        mydb.commit()
        
    except Exception as e:
        print(e)
        
    finally:
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
    

def getReviewsWindow():
    global reviewsWindow
    return(reviewsWindow)

def setReviewsWindow(newWindow):
    global reviewsWindow
    reviewsWindow = newWindow

def closeReviewsWindow():
    global reviewsWindow
    reviewsWindow.destroy()
    reviewsWindow = None


def getReturnWindow():
    global returnWindow
    return(returnWindow)

def setReturnWindow(newWindow):
    global returnWindow
    returnWindow = newWindow

def closeReturnWindow():
    global returnWindow
    returnWindow.destroy()
    returnWindow = None


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


def setPassword(newPassword):
    global password
    password = newPassword
    
def getPassword():
    global password
    return(password)


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