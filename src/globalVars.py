import mysql.connector

# window object
window = None
# flag to keep track of the login
loggedIn = False # MOCK DATA
# flag to keep track of the program execution
running = True
# string for the logged in user
user = "" # MOCK DATA

booksOwned = 20 # MOCK DATA

strings = dict()

ints = dict()

# MySQL database connection
mydb = mysql.connector.connect(
			host = "localhost",
			user = "josh",
			password = "password",
			database = "biblioteca"
		)
# cursor to issue commands to the database
cursor = mydb.cursor(buffered = True)

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
    
    except Exception as e:
        print(e)

    finally:
        # commit the changes to the database
        mydb.commit()
        # return the result of the command
        return(result)



# SETTERS AND GETTERS FOR GLOBAL VARIABLES
def getWindow():
    global window
    return(window)

def setWindow(newWindow):
    global window
    window = newWindow


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