# STYLE module for applying a style to the tkinter window

# ttk module for styled tkinter windows
from tkinter.ttk import *

# function to set the dark theme of "azure" to the selected window
def loadStyle(currentWindow):    
    currentWindow.tk.call("source", "./themes/azure/azure.tcl")
    currentWindow.tk.call("set_theme", "dark")