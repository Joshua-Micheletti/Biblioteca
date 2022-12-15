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

    getWindow().rowconfigure(0, weight = 0)
    getWindow().rowconfigure(1, weight = 9)
    getWindow().rowconfigure(2, weight = 0)
    getWindow().columnconfigure(0, weight = 0)
    getWindow().columnconfigure(1, weight = 5)
    getWindow().columnconfigure(2, weight = 0)
    #getWindow().rowconfigure(1, weight = 0)

    relief = "flat"

    # create the frame for the app
    appFUserInfo = Frame(getWindow())
    appFUserInfo["relief"] = relief
    appFUserInfo.grid(column = 0, row = 0, sticky = "nsew")
    #appFNW.rowconfigure(0, weight = 1)
    #appFNW.columnconfigure(0, weight = 1)

    appFDisplayOptions = Frame(getWindow())
    appFDisplayOptions["relief"] = relief
    appFDisplayOptions.grid(column = 1, row = 0, sticky = "nsew")

    appFSearch = Frame(getWindow())
    appFSearch["relief"] = relief
    appFSearch.grid(column = 2, row = 0, sticky = "nsew")

    appFDatabase = Frame(getWindow())
    appFDatabase["relief"] = relief
    appFDatabase.grid(column = 0, row = 1, columnspan = 3, sticky = "nsew")

    appFCC = Frame(getWindow())
    appFCC["relief"] = relief
    #appFCC.grid(column = 1, row = 1, sticky = "nsew")

    appFCE = Frame(getWindow())
    appFCE["relief"] = relief
    #appFCE.grid(column = 2, row = 1, sticky = "nsew")

    appFLogout = Frame(getWindow())
    appFLogout["relief"] = relief
    appFLogout.grid(column = 0, row = 2, sticky = "nsew")

    appFSC = Frame(getWindow())
    appFSC["relief"] = relief
    appFSC.grid(column = 1, row = 2, sticky = "nsew")

    appFSE = Frame(getWindow())
    appFSE["relief"] = relief
    appFSE.grid(column = 2, row = 2, sticky = "nsew")


    # load the app frame
    frames["appFUserInfo"] = appFUserInfo
    frames["appFDisplayOptions"] = appFDisplayOptions
    frames["appFSearch"] = appFSearch
    frames["appFDatabase"] = appFDatabase
    frames["appFCC"] = appFCC
    frames["appFCE"] = appFCE
    frames["appFLogout"] = appFLogout
    frames["appFSC"] = appFSC
    frames["appFSE"] = appFSE

    # return all the frames
    return(frames)
    

def loadSearchFrames():
    frames = dict()

    getSearchWindow().rowconfigure(0, weight = 1)
    getSearchWindow().columnconfigure(0, weight = 1)

    searchFrame = Frame(getSearchWindow())

    searchFrame.grid(column = 0, row = 0, sticky = "nsew")

    searchFrame.rowconfigure(0, weight = 1)
    searchFrame.rowconfigure(1, weight = 1)
    searchFrame.rowconfigure(2, weight = 1)
    searchFrame.rowconfigure(3, weight = 1)
    searchFrame.rowconfigure(4, weight = 1)
    searchFrame.rowconfigure(5, weight = 1)
    searchFrame.rowconfigure(6, weight = 1)
    searchFrame.columnconfigure(0, weight = 0)
    searchFrame.columnconfigure(1, weight = 3)

    searchButtonsFrame = Frame(searchFrame)

    searchButtonsFrame.grid(column = 0, row = 6, columnspan = 2, sticky = "nsew")

    searchButtonsFrame.rowconfigure(0, weight = 0)
    searchButtonsFrame.columnconfigure(0, weight = 0)
    searchButtonsFrame.columnconfigure(1, weight = 0)
    searchButtonsFrame.columnconfigure(2, weight = 2)

    frames["searchFrame"] = searchFrame
    frames["searchButtonsFrame"] = searchButtonsFrame

    return(frames)


    