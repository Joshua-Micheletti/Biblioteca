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
    getWindow().rowconfigure(2, weight = 1)
    getWindow().columnconfigure(0, weight = 0)
    getWindow().columnconfigure(1, weight = 5)
    getWindow().columnconfigure(2, weight = 0)
    #getWindow().rowconfigure(1, weight = 0)

    relief = "flat"

    # create the frame for the app
    appFNW = Frame(getWindow())
    appFNW["relief"] = relief
    appFNW.grid(column = 0, row = 0, sticky = "nsew")
    #appFNW.rowconfigure(0, weight = 1)
    #appFNW.columnconfigure(0, weight = 1)

    appFNC = Frame(getWindow())
    appFNC["relief"] = relief
    appFNC.grid(column = 1, row = 0, sticky = "nsew")

    appFNE = Frame(getWindow())
    appFNE["relief"] = relief
    appFNE.grid(column = 2, row = 0, sticky = "nsew")

    appFCW = Frame(getWindow())
    appFCW["relief"] = relief
    appFCW.grid(column = 0, row = 1, columnspan = 3, sticky = "nsew")

    appFCC = Frame(getWindow())
    appFCC["relief"] = relief
    #appFCC.grid(column = 1, row = 1, sticky = "nsew")

    appFCE = Frame(getWindow())
    appFCE["relief"] = relief
    #appFCE.grid(column = 2, row = 1, sticky = "nsew")

    appFSW = Frame(getWindow())
    appFSW["relief"] = relief
    appFSW.grid(column = 0, row = 2, sticky = "nsew")

    appFSC = Frame(getWindow())
    appFSC["relief"] = relief
    appFSC.grid(column = 1, row = 2, sticky = "nsew")

    appFSE = Frame(getWindow())
    appFSE["relief"] = relief
    appFSE.grid(column = 2, row = 2, sticky = "nsew")


    # load the app frame
    frames["appFNW"] = appFNW
    frames["appFNC"] = appFNC
    frames["appFNE"] = appFNE
    frames["appFCW"] = appFCW
    frames["appFCC"] = appFCC
    frames["appFCE"] = appFCE
    frames["appFSW"] = appFSW
    frames["appFSC"] = appFSC
    frames["appFSE"] = appFSE



    # return all the frames
    return(frames)
    

    