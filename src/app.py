# MAIN module for the application, this is there the program starts and where the main function is located

# module for creating widgets to populate frames
from widgets import *
# module for creating frames to populate windows
from frames import *
# module for sharing variables and constructs
from globalVars import *
# module for creating and managing windows
from window import *

# MAIN FUNCTION
def main():
    # create a window for as long as the program is running
    # if the user is not logged in
    if not getLogin():
        # create the login window
        createLoginWindow()
        # load its frames and widgets
        loadWidgets(loadLoginFrames())
        # run the window
        getWindow().mainloop()

    # if the user is logged in
    else:
        # create the app window
        createAppWindow()
        # load its widgets and frames
        loadWidgets(loadAppFrames())
        # run the window
        getWindow().mainloop()

    
# start of the program
if __name__ == "__main__":
    main()