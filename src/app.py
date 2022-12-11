from tkinter import *
from widgets import *
from frames import *
from style import *
from globalVars import *
from window import *
from ttkthemes import ThemedTk

# MAIN FUNCTION
def main():
    # create a window for as long as the program is running
    while getRunning():
        
        if not getLogin():
            createLoginWindow()
            loadWidgets(loadLoginFrames()) # load the frames and the widgets
            getWindow().mainloop()                       # run the app

        else:
            createAppWindow()
            loadWidgets(loadAppFrames())
            getWindow().mainloop()

        print("test")

    
# start of the program
if __name__ == "__main__":
    main()