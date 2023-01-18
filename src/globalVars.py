# GLOBALVARS module for sharing global variables and objects across all modules

# module for connecting to the MySQL database
import mysql.connector

# main window object
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
loggedIn = False
# string for the logged in user
user = ""
password = ""
# variable for keeping track of the book owned by the user
booksOwned = ""

# dictionary of StringVar used in the app
strings = dict()

# object to store the connection to the database
mydb = None

try:
    # MySQL database connection
    mydb = mysql.connector.connect(
                host = "solidgallium.ddns.net", # database IP (default port 3306)
                user = "josh",                  # username
                password = "password",          # password
                database = "biblioteca"         # database to use
            )
    
    # cursor to issue commands to the database
    cursor = mydb.cursor(buffered = True)
    
# catch any exception in case the database is not reachable
except Exception as e:
    print(e)


# function to send commands to the database
def sendMySQL(command):
    global mydb

    # variable for storing the result of the query
    result = None

    try:
        # send the MySQL command
        cursor.execute(command)
        print(cursor)
        # store the result
        result = cursor.fetchall()
        # commit the changes to the database
        mydb.commit()
    
    # catch any exception
    except Exception as e:
        print(e)

    finally:
        # return the result of the command
        return(result)


# SETTERS AND GETTERS FOR GLOBAL VARIABLES
# get main window object
def getWindow():
    global window
    return(window)
# set main window object
def setWindow(newWindow):
    global window
    window = newWindow
# function to close the program
def closeProgram():
    global window
    window.destroy()

# get search window object
def getSearchWindow():
    global searchWindow
    return(searchWindow)
# set search window object
def setSearchWindow(newWindow):
    global searchWindow
    searchWindow = newWindow
# close search window
def closeSearchWindow():
    global searchWindow
    searchWindow.destroy()
    searchWindow = None

# get book window object
def getBookWindow():
    global bookWindow
    return(bookWindow)
# set book window object
def setBookWindow(newWindow):
    global bookWindow
    bookWindow = newWindow
# close the book window
def closeBookWindow():
    global bookWindow
    bookWindow.destroy()
    bookWindow = None
    
# get reviews window object
def getReviewsWindow():
    global reviewsWindow
    return(reviewsWindow)
# set reviews window object
def setReviewsWindow(newWindow):
    global reviewsWindow
    reviewsWindow = newWindow
# close the reviews window
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
