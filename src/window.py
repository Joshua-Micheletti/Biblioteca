from tkinter import *
from ttkthemes import ThemedTk
from globalVars import *
from style import *

def closeProgramCallback(event):
    setRunning(False)
    getWindow().destroy()

def closeSearchWindowCallback(event):
    getSearchWindow().destroy()


# function to create windows
def createAppWindow():
    window = getWindow()
    window = ThemedTk()
    window.geometry("1280x720")
    window.title("Libreria")
    window.resizable(FALSE, FALSE)
    window.bind('<Escape>', closeProgramCallback)

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

    #loadStyle(searchWindow)
    setSearchWindow(searchWindow)

    return(searchWindow)