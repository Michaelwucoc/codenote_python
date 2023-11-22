i = 0
x = 12345678
while i == 0:
    y = int (input("Please enter the password. \n"))
    
    if x == y:
        print ("Logged in to the server.")
        break
    else:
        print ("Password incorrect. Please try again.")