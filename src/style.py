from tkinter.ttk import *
from globalVars import *

def loadStyle(currentWindow):    
    currentWindow.tk.call("source", "./themes/azure/azure.tcl")
    currentWindow.tk.call("set_theme", "dark")