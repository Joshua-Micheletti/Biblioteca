from tkinter import *
from widgets import *
from frames import *
from style import *
from globalVars import *
from ttkthemes import ThemedTk

# callback function to close the program
def closeProgram(event):
    global running

    running = False
    getWindow().destroy()

# function to create windows
def createWindow():
    # get the reference to the window
    window = getWindow()
    
    # if the user isn't logged in
    # create a login window
    if not getLogin():
        window = ThemedTk()                     # create the window
        window.geometry("500x300")             # "500x200+offsetx+offsety"
        window.title("Login")                 # set the window name
        window.resizable(FALSE, FALSE)            # resizable width and height
        window.minsize(500, 300)                # min resize dimensions
        window.attributes('-alpha', 1)          # opacity
        #window.attributes('-topmost', 1)       # window always on top
        window.iconphoto(False, PhotoImage(file = './data/icon.png')) # load the icon
        window.bind('<Escape>', closeProgram)   # bind the escape button to close the program
        
        setWindow(window)

        loadStyle()
        loadWidgets(loadLoginFrames()) # load the frames and the widgets
        
        window.mainloop()                       # run the app

    # if the user is logged in
    # load the app window
    if getLogin():
        window = ThemedTk()
        window.geometry("1280x720")
        window.title("Libreria")
        window.resizable(FALSE, FALSE)
        window.bind('<Escape>', closeProgram)

        setWindow(window)

        loadStyle()
        loadWidgets(loadAppFrames())

        window.mainloop()


# MAIN FUNCTION
def main():
    global running
    # create a window for as long as the program is running
    while running:
        createWindow()

    
# start of the program
if __name__ == "__main__":
    main()