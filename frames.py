from app import *
from widgets import *
from tkinter.ttk import *

def loadLoginFrames(window):
    frames = dict()

    window.columnconfigure(0, weight = 2)
    window.rowconfigure(0, weight = 1)
    window.rowconfigure(1, weight = 0)

    loginF = Frame(window)
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

    frames["loginF"] = loginF

    return(frames)


def loadAppFrames(window):
    frames = dict()

    appF = Frame(window)

    frames["appF"] = appF

    return(frames)
    

    