# FRAMES module for creating frames to populate windows

# module for sharing variables and constructs
from globalVars import *
# module for creating styled frames
from tkinter.ttk import *

# function for loading the frame for the login UI
def loadLoginFrames():
    # create an empty dictionary of frames
    frames = dict()

    # configure the grid of the main window
    getWindow().columnconfigure(0, weight = 2)
    getWindow().rowconfigure(0, weight = 1)
    getWindow().rowconfigure(1, weight = 0)

    # create a login frame
    loginF = Frame(getWindow())
    loginF["padding"] = (20, 20)
    loginF["relief"] = "flat" # flat, raised, sunken, groove, ridge
    loginF.grid(column = 0, row = 0, sticky="nsew")
    loginF.rowconfigure(0, weight = 1)
    loginF.rowconfigure(1, weight = 1)
    loginF.rowconfigure(2, weight = 1)
    loginF.rowconfigure(3, weight = 1)
    loginF.rowconfigure(4, weight = 2)
    loginF.rowconfigure(5, weight = 2)
    loginF.columnconfigure(0, weight = 1)

    # load the login frames
    frames["loginF"] = loginF

    # return all the frames
    return(frames)

# function for loading the frame for the main app UI
def loadAppFrames():
    # create an empty dictionary of frames
    frames = dict()

    # configure the grid for the main window
    getWindow().rowconfigure(0, weight = 0)
    getWindow().rowconfigure(1, weight = 9)     
    getWindow().rowconfigure(2, weight = 0)     # |NW|NC|NE|
    getWindow().columnconfigure(0, weight = 0)  # |CW|CC|CE|
    getWindow().columnconfigure(1, weight = 5)  # |SW|SC|SE|
    getWindow().columnconfigure(2, weight = 0)
    
    # variable for changing the borders of the frames (useful for telling the limits of each frame)
    relief = "flat" # change to "groove" to better visualize the frame borders

    # create the frames for the app
    
    # user info frame (North-West)
    appFUserInfo = Frame(getWindow())
    appFUserInfo["relief"] = relief
    appFUserInfo.grid(column = 0, row = 0, sticky = "nsew")

    # frame containing features for borrowing and returning books (North-Center)
    appFManageBook = Frame(getWindow())
    appFManageBook["relief"] = relief
    appFManageBook.grid(column = 1, row = 0, sticky = "nsew")

    # search feature frame (North-East)
    appFSearch = Frame(getWindow())
    appFSearch["relief"] = relief
    appFSearch.grid(column = 2, row = 0, sticky = "nsew")

    # database frame containing info about the books in the library (Center-West to Center-East)
    appFDatabase = Frame(getWindow())
    appFDatabase["relief"] = relief
    appFDatabase.grid(column = 0, row = 1, columnspan = 3, sticky = "nsew")

    # unused frames since the database frame spans over both of them
    appFCC = Frame(getWindow())
    appFCC["relief"] = relief

    appFCE = Frame(getWindow())
    appFCE["relief"] = relief

    # logout frame (close and logout features) (South-West)
    appFLogout = Frame(getWindow())
    appFLogout["relief"] = relief
    appFLogout.grid(column = 0, row = 2, sticky = "nsew")

    # review frame (South-Center)
    appFReview = Frame(getWindow())
    appFReview["relief"] = relief
    appFReview.grid(column = 1, row = 2, sticky = "nsew")

    # modify library frame (add, remove, modify book(s)) (South-East)
    appFModifyLibrary = Frame(getWindow())
    appFModifyLibrary["relief"] = relief
    appFModifyLibrary.grid(column = 2, row = 2, sticky = "nsew")


    # load the frames into the dictionary
    frames["appFUserInfo"] = appFUserInfo
    frames["appFManageBook"] = appFManageBook
    frames["appFSearch"] = appFSearch
    frames["appFDatabase"] = appFDatabase
    frames["appFCC"] = appFCC
    frames["appFCE"] = appFCE
    frames["appFLogout"] = appFLogout
    frames["appFReview"] = appFReview
    frames["appFModifyLibrary"] = appFModifyLibrary

    # return all the frames
    return(frames)
    
# function for loading the frame for the search window UI
def loadSearchFrames():
    # create an empty dictionary for the frames
    frames = dict()

    # configure the grid of the main window
    getSearchWindow().rowconfigure(0, weight = 1)
    getSearchWindow().columnconfigure(0, weight = 1)

    # create a frame for the search window
    searchFrame = Frame(getSearchWindow())
    searchFrame.grid(column = 0, row = 0, sticky = "nsew")

    # divide the frame in a 7x2 grid
    searchFrame.rowconfigure(0, weight = 1)
    searchFrame.rowconfigure(1, weight = 1)
    searchFrame.rowconfigure(2, weight = 1)
    searchFrame.rowconfigure(3, weight = 1)
    searchFrame.rowconfigure(4, weight = 1)
    searchFrame.rowconfigure(5, weight = 1)
    searchFrame.rowconfigure(6, weight = 1)
    searchFrame.columnconfigure(0, weight = 0)
    searchFrame.columnconfigure(1, weight = 3)

    # create a frame for the buttons in the search window
    searchButtonsFrame = Frame(searchFrame)
    searchButtonsFrame.grid(column = 0, row = 6, columnspan = 2, sticky = "nsew")

    # divide the frame in a 1x3 grid
    searchButtonsFrame.rowconfigure(0, weight = 0)
    searchButtonsFrame.columnconfigure(0, weight = 0)
    searchButtonsFrame.columnconfigure(1, weight = 0)
    searchButtonsFrame.columnconfigure(2, weight = 2)

    # load the frames into the dictionary
    frames["searchFrame"] = searchFrame
    frames["searchButtonsFrame"] = searchButtonsFrame

    # return all the frames
    return(frames)

# function for loading the frame for the book window UI
def loadBookFrames(function):
    # create an empty dictionary for the frames
    frames = dict()

    # configure the grid of the window
    getBookWindow().rowconfigure(0, weight = 1)
    getBookWindow().columnconfigure(0, weight = 1)

    # create a frame for the book window
    bookFrame = Frame(getBookWindow())
    bookFrame.grid(column = 0, row = 0, sticky = "nsew")

    # divide the frame in a 7x2 grid
    bookFrame.rowconfigure(0, weight = 1)
    bookFrame.rowconfigure(1, weight = 1)
    bookFrame.rowconfigure(2, weight = 1)
    bookFrame.rowconfigure(3, weight = 1)
    bookFrame.rowconfigure(4, weight = 1)
    bookFrame.rowconfigure(5, weight = 1)
    bookFrame.rowconfigure(6, weight = 1)
    bookFrame.columnconfigure(0, weight = 0)
    bookFrame.columnconfigure(1, weight = 3)

    # create a frame for the buttons on the book window
    bookFunctionsFrame = Frame(bookFrame)
    bookFunctionsFrame.grid(column = 0, row = 6, columnspan = 2, sticky = "nsew")

    # divide the frame in a 1x2 grid
    bookFunctionsFrame.rowconfigure(0, weight = 1)
    bookFunctionsFrame.columnconfigure(0, weight = 0)
    bookFunctionsFrame.columnconfigure(1, weight = 3)

    # store the frames in the dictionary
    frames["bookFrame"] = bookFrame
    
    # depending on the argument of the function, load the functions frame with different names
    # this will make it so that different widgets will be loaded into them depending on the name
    if function == "add":
        frames["bookAddFrame"] = bookFunctionsFrame
    elif function == "modify":
        frames["bookModifyFrame"] = bookFunctionsFrame

    # return all the frames
    return(frames)
    
# function for loading the frame for the reviews window UI
def loadReviewsFrame():
    # create an empty dictionary for the frames
    frames = dict()
    
    # configure the grid of the window
    getReviewsWindow().rowconfigure(0, weight = 1)
    getReviewsWindow().columnconfigure(0, weight = 1)
    
    # create a frame for the window
    reviewsFrame = Frame(getReviewsWindow())
    reviewsFrame.grid(column = 0, row = 0, sticky = "nsew")
    
    # divide the frame in a 2x1 grid
    reviewsFrame.rowconfigure(0, weight = 1)
    reviewsFrame.rowconfigure(1, weight = 1)
    reviewsFrame.columnconfigure(0, weight = 1)
    
    # store the frame in the dictionary
    frames["reviewsFrame"] = reviewsFrame
    
    # return all the frames
    return(frames)

# function for loading the frame for the return window UI
def loadReturnFrame():
    # create an empty dictionary for the frames
    frames = dict()
    
    # configure the window grid
    getReturnWindow().rowconfigure(0, weight = 1)
    getReturnWindow().columnconfigure(0, weight = 1)
    
    # create the frame for the return window
    returnFrame = Frame(getReturnWindow())
    returnFrame.grid(column = 0, row = 0, sticky = "nsew")
    
    # divide the frame in a 6x2 grid
    returnFrame.rowconfigure(0, weight = 1)
    returnFrame.rowconfigure(1, weight = 1)
    returnFrame.rowconfigure(2, weight = 1)
    returnFrame.rowconfigure(3, weight = 1)
    returnFrame.rowconfigure(4, weight = 1)
    returnFrame.rowconfigure(5, weight = 1)
    returnFrame.columnconfigure(0, weight = 1)
    returnFrame.columnconfigure(1, weight = 1)
    
    # store the frame in the dictionary
    frames["returnFrame"] = returnFrame
    
    # return the frames
    return(frames)