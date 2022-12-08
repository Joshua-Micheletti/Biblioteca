from tkinter.ttk import *
from globalVars import *

def loadStyle():
    window = getWindow()

    style = Style(window)
    
    window.tk.call("source", "./themes/azure/azure.tcl")
    window.tk.call("set_theme", "dark")

    style.configure("Warning.TLabel",
        foreground = "#f0ad4e",
        font = ("Arial", 40)
    )

    style.configure("TLabel",
        font = ("Arial", 30)
    )

    setWindow(window)

    #style.configure(".", font = ("Arial", 30))