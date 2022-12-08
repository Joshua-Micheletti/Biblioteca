from tkinter import *
from widgets import *
from frames import *
from style import *
from globalVars import *
from ttkthemes import ThemedTk

def closeProgram(event):
    global window
    global running

    running = False
    window.destroy()
    print(window)

def createWindow():
    global window
    
    if not getLogin():
        window = ThemedTk()                     # create the window
        window.geometry("500x300")             # "500x200+offsetx+offsety"
        window.title("Progetto")                 # set the window name
        window.resizable(FALSE, FALSE)            # resizable width and height
        window.minsize(500, 300)                # min resize dimensions
        window.attributes('-alpha', 1)          # opacity
        #window.attributes('-topmost', 1)       # window always on top
        window.iconphoto(False, PhotoImage(file = './data/icon.png')) # load the icon
        window.bind('<Escape>', closeProgram)   # bind the escape button to close the program
        
        loadStyle(window)
        loadWidgets(loadLoginFrames(window), window) # load the frames and the widgets
        
        window.mainloop()                       # run the app

    if getLogin():
        window = ThemedTk()
        window.geometry("1280x720")
        window.title("Libreria")
        window.resizable(FALSE, FALSE)
        window.bind('<Escape>', closeProgram)

        loadStyle(window)
        loadWidgets(loadAppFrames(window), window)

        window.mainloop()

def main():
    global window
    global loggedIn
    global running

    while running:
        print(loggedIn)
        createWindow()

    

if __name__ == "__main__":
    main()