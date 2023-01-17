from tkinter import *
from ttkthemes import ThemedTk
from globalVars import *
from style import *

def closeProgramCallback(event):
    setRunning(False)
    getWindow().destroy()
    
def closeProgramWindowManager():
    setRunning(False)
    getWindow().destroy()
    

def closeSearchWindowCallback(event):
    getSearchWindow().destroy()
    setSearchWindow(None)
    
def closeSearchWindowManager():
    getSearchWindow().destroy()
    setSearchWindow(None)
    

def closeBookWindowCallback(event):
    getBookWindow().destroy()
    setBookWindow(None)
    
def closeBookWindowManager():
    getBookWindow().destroy()
    setBookWindow(None)
    
    
def closeReviewsWindowCallback(event):
    getReviewsWindow().destroy()
    setReviewsWindow(None)
    
def closeReviewsWindowManager():
    getReviewsWindow().destroy()
    setReviewsWindow(None)
    
    
def closeReturnWindowCallback(event):
    getReturnWindow().destroy()
    setReturnWindow(None)
    
def closeReturnWindowManager():
    getReturnWindow().destroy()
    setReturnWindow(None)




# function to create windows
def createAppWindow():
    window = getWindow()
    window = ThemedTk()
    window.geometry("1280x720")
    window.title("Libreria")
    window.resizable(FALSE, FALSE)
    window.bind('<Escape>', closeProgramCallback)
    window.protocol("WM_DELETE_WINDOW", closeProgramWindowManager)

    loadStyle(window)
    setWindow(window)

def createLoginWindow():
    # get the reference to the window
    window = getWindow()
    
    # if the user isn't logged in
    # create a login window
    window = ThemedTk()                     # create the window
    window.geometry("500x300")             # "500x200+offsetx+offsety"
    window.title("Login")                 # set the window name
    window.resizable(FALSE, FALSE)            # resizable width and height
    window.minsize(500, 300)                # min resize dimensions
    window.attributes('-alpha', 1)          # opacity
    #window.attributes('-topmost', 1)       # window always on top
    window.iconphoto(False, PhotoImage(file = './data/icon.png')) # load the icon
    window.bind('<Escape>', closeProgramCallback)   # bind the escape button to close the program
    window.protocol("WM_DELETE_WINDOW", closeProgramWindowManager)
    
    loadStyle(window)
    setWindow(window)

def createSearchWindow():
    searchWindow = getSearchWindow()

    searchWindow = Toplevel()                     # create the window
    searchWindow.geometry("500x300")             # "500x200+offsetx+offsety"
    searchWindow.title("Login")                 # set the window name
    searchWindow.resizable(FALSE, FALSE)            # resizable width and height
    searchWindow.minsize(500, 300)                # min resize dimensions
    searchWindow.attributes('-alpha', 1)          # opacity
    #window.attributes('-topmost', 1)       # window always on top
    #searchWindow.iconphoto(False, PhotoImage(file = './data/icon.png')) # load the icon
    searchWindow.bind('<Escape>', closeSearchWindowCallback)   # bind the escape button to close the program
    searchWindow.protocol("WM_DELETE_WINDOW", closeSearchWindowManager)

    #loadStyle(searchWindow)
    setSearchWindow(searchWindow)

    return(searchWindow)


def createBookWindow():
    bookWindow = getBookWindow()

    bookWindow = Toplevel()
    bookWindow.geometry("500x300")
    bookWindow.title("Libro")
    bookWindow.resizable(FALSE, FALSE)
    bookWindow.minsize(500, 300)
    bookWindow.attributes('-alpha', 1)
    bookWindow.bind('<Escape>', closeBookWindowCallback)
    bookWindow.protocol("WM_DELETE_WINDOW", closeBookWindowManager)

    setBookWindow(bookWindow)

    return(bookWindow)


def createReviewsWindow():
    reviewsWindow = getReviewsWindow()

    reviewsWindow = Toplevel()
    reviewsWindow.geometry("500x300")
    reviewsWindow.title("Recensioni")
    reviewsWindow.resizable(FALSE, FALSE)
    reviewsWindow.minsize(500, 300)
    reviewsWindow.attributes('-alpha', 1)
    reviewsWindow.bind('<Escape>', closeReviewsWindowCallback)
    reviewsWindow.protocol("WM_DELETE_WINDOW", closeReviewsWindowManager)

    setReviewsWindow(reviewsWindow)

    return(reviewsWindow)



def createReturnWindow():
    returnWindow = getReturnWindow()

    returnWindow = Toplevel()
    returnWindow.geometry("500x300")
    returnWindow.title("Restituzione")
    returnWindow.resizable(FALSE, FALSE)
    returnWindow.minsize(500, 300)
    returnWindow.attributes('-alpha', 1)
    returnWindow.bind('<Escape>', closeReturnWindowCallback)
    returnWindow.protocol("WM_DELETE_WINDOW", closeReturnWindowManager)

    setReturnWindow(returnWindow)

    return(returnWindow)


