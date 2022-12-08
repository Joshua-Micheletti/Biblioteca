from app import *
from widgets import *
from globalVars import *
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

    # create the frame for the app
    appF = Frame(getWindow())

    # load the app frame
    frames["appF"] = appF

    # return all the frames
    return(frames)
    

    