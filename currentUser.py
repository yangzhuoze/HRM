from main.Models import Clerk

currentUser = None

def getCurrentUser():
    global currentUser
    return currentUser
  
def setCurrentUser(User):
    global currentUser
    currentUser = User
