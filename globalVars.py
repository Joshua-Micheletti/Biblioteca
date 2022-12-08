window = None
loggedIn = False
running = True

def checkLoggedIn():
    global loggedIn
    print(loggedIn)

def setLogin(flag):
    global loggedIn
    loggedIn = flag

def getLogin():
    global loggedIn
    return(loggedIn)