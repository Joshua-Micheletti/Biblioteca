# LOGIN module for logging in and registering new users

# module for applying a hash function to the password
from hashlib import sha256
# module to access global variables and constructs
from globalVars import *

# LOGIN FUNCTION
def login(username, password):
    # apply a hash function to the password
    hashedPassword = sha256(password.encode('utf-8')).hexdigest()
    # send a query to check if the user and password match
    result = sendMySQL("SELECT * " +
                       "FROM utenti " +
                       "WHERE Nome='" + username + "'" +
                       "AND Password='" + hashedPassword + "';")
    # if they match
    if len(result) != 0:
        print(len(result))
        print(result[0][2])
        
        if result[0][2] != None:
            bookName = sendMySQL("SELECT Titolo " +
                                 "FROM libri " +
                                 "WHERE ID = " + str(result[0][2]))
            setBooksOwned(bookName[0][0])
        
        return(True)
    
    # if they don't match
    else:
        return(False)


# REGISTER FUNCTION
def register(username, password):
    # apply a hash function to the password
    hashedPassword = sha256(password.encode('utf-8')).hexdigest()
    # check if the user already exists in the database
    result = sendMySQL("SELECT Nome " +
                       "FROM utenti " +
                       "WHERE Nome='" + username + "';")

    # if it doesn't exist
    if len(result) == 0:
        # create a new entry in the users table
        result = sendMySQL("INSERT INTO utenti(Nome, Password) " + 
                           "VALUES ('" + username + "', '" + hashedPassword + "');")
        
        return(True)

    # if the user already exists
    else:
        return(False)
