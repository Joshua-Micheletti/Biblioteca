# WINDOW module for creating and closing windows

# module for creating tkinter windows
from tkinter import *
# module for creating themed tkinter windows
from ttkthemes import ThemedTk
# module for accessing global variables and constructs
from globalVars import *
# module for applying a style to a tkinter window
from style import *

# callback function to close the program after a user input
def closeProgramCallback(event):
    getWindow().destroy()
# callback function to close the program after a window manager close signal (X)
def closeProgramWindowManager():
    getWindow().destroy()
    
# callback function to close the search window after a user input
def closeSearchWindowCallback(event):
    getSearchWindow().destroy()
    setSearchWindow(None)
# callback function to close the search window after a window manager close signal (X)
def closeSearchWindowManager():
    getSearchWindow().destroy()
    setSearchWindow(None)
    
# callback function to close the book window after a user input
def closeBookWindowCallback(event):
    getBookWindow().destroy()
    setBookWindow(None)
# callback function to close the book window after a window manager close signal (X)  
def closeBookWindowManager():
    getBookWindow().destroy()
    setBookWindow(None)
    
# callback function to close the reviews window after a user input
def closeReviewsWindowCallback(event):
    getReviewsWindow().destroy()
    setReviewsWindow(None)
# callback function to close the reviews window after a window manager close signal (X)
def closeReviewsWindowManager():
    getReviewsWindow().destroy()
    setReviewsWindow(None)
    
# callback function to close the return window after a user input
def closeReturnWindowCallback(event):
    getReturnWindow().destroy()
    setReturnWindow(None)
# callback function to close the return window after a window manager close signal (X)
def closeReturnWindowManager():
    getReturnWindow().destroy()
    setReturnWindow(None)


# function to create the main app window
def createAppWindow():
    # get a reference to the window global object
    window = getWindow()
    # initialize it as a themed tkinter window
    window = ThemedTk()
    # initialize the resolution
    window.geometry("1280x720")
    # give it a title
    window.title("Libreria")
    # set it to not be resizable
    window.resizable(FALSE, FALSE)
    # bind the Escape key to close the window
    window.bind('<Escape>', closeProgramCallback)
    # bind the Delete signal to the callback function
    window.protocol("WM_DELETE_WINDOW", closeProgramWindowManager)

    # load the style to the window
    loadStyle(window)
    # store the newly created object to be globally shared
    setWindow(window)

# function to create the login window
def createLoginWindow():
    # get the reference to the window
    window = getWindow()
    
    window = ThemedTk()                    # create the window
    window.geometry("500x300")             # "500x300+offsetx+offsety"
    window.title("Login")                  # set the window name
    window.resizable(FALSE, FALSE)         # resizable width and height
    window.minsize(500, 300)               # min resize dimensions
    window.attributes('-alpha', 1)         # opacity
    # bind the escape button to close the program
    window.bind('<Escape>', closeProgramCallback)
    # bind the Delete signal to the callback function
    window.protocol("WM_DELETE_WINDOW", closeProgramWindowManager)
    
    # load the style to the window
    loadStyle(window)
    # store the newly created object to be globally shared
    setWindow(window)

# function to create the toplevel search window
def createSearchWindow():
    # get the reference to the window
    searchWindow = getSearchWindow()

    searchWindow = Toplevel()               # create the window
    searchWindow.geometry("500x300")        # "500x300+offsetx+offsety"
    searchWindow.title("Cerca")             # set the window name
    searchWindow.resizable(FALSE, FALSE)    # resizable width and height
    searchWindow.minsize(500, 300)          # min resize dimensions
    searchWindow.attributes('-alpha', 1)    # opacity
    # bind the escape button to close the window
    searchWindow.bind('<Escape>', closeSearchWindowCallback)
    # bind the Delete signal to the callback function  
    searchWindow.protocol("WM_DELETE_WINDOW", closeSearchWindowManager)

    # store the newly created object to be globally shared
    setSearchWindow(searchWindow)

    return(searchWindow)

# function to create the toplevel book window
def createBookWindow():
    # get the reference to the window
    bookWindow = getBookWindow()

    bookWindow = Toplevel()             # create the window
    bookWindow.geometry("500x300")      # "500x300+offsetx+offsety"
    bookWindow.title("Libro")           # set the window name
    bookWindow.resizable(FALSE, FALSE)  # resizable width and height
    bookWindow.minsize(500, 300)        # min resize dimensions
    bookWindow.attributes('-alpha', 1)  # opacity
    # bind the escape button to close the window
    bookWindow.bind('<Escape>', closeBookWindowCallback)
    # bind the Delete signal to the callback function  
    bookWindow.protocol("WM_DELETE_WINDOW", closeBookWindowManager)

    # store the newly created object to be globally shared
    setBookWindow(bookWindow)

    return(bookWindow)

# function to create the toplevel reviews window
def createReviewsWindow():
    # get the reference to the window
    reviewsWindow = getReviewsWindow()

    reviewsWindow = Toplevel()              # create the window  
    reviewsWindow.geometry("500x300")       # "500x300+offsetx+offsety"
    reviewsWindow.title("Recensioni")       # set the window name
    reviewsWindow.resizable(FALSE, FALSE)   # resizable width and height
    reviewsWindow.minsize(500, 300)         # min resize dimensions
    reviewsWindow.attributes('-alpha', 1)   # opacity
    # bind the escape button to close the window
    reviewsWindow.bind('<Escape>', closeReviewsWindowCallback)
    # bind the Delete signal to the callback function  
    reviewsWindow.protocol("WM_DELETE_WINDOW", closeReviewsWindowManager)

    # store the newly created object to be globally shared
    setReviewsWindow(reviewsWindow)

    return(reviewsWindow)

# function to create the toplevel return window
def createReturnWindow():
    # get the reference to the window
    returnWindow = getReturnWindow()

    returnWindow = Toplevel()               # create the window
    returnWindow.geometry("500x300")        # "500x300+offsetx+offsety"
    returnWindow.title("Restituzione")      # set the window name
    returnWindow.resizable(FALSE, FALSE)    # resizable width and height
    returnWindow.minsize(500, 300)          # min resize dimensions
    returnWindow.attributes('-alpha', 1)    # opacity
    # bind the escape button to close the window
    returnWindow.bind('<Escape>', closeReturnWindowCallback)
    # bind the Delete signal to the callback function 
    returnWindow.protocol("WM_DELETE_WINDOW", closeReturnWindowManager)

    # store the newly created object to be globally shared
    setReturnWindow(returnWindow)

    return(returnWindow)