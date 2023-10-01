password = input("Enter password: ")

while password != "admin792": # '!=' means not equal
    if password[0] == "a":
        print("You got the first letter correct")
    else:
        print("Wrong password")
    password = input("Enter password") # Try again, after this line the code will go to line 3 again.
    
print("You're in")