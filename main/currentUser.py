currentUser = None

def getCurrentUser():
    global currentUser
    return currentUser
  
def setCurrentUser(User):
    global currentUser
    currentUser = User
