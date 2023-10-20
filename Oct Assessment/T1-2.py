pwd = input("Enter a password:")
savedPwd = "topsecret00"

while pwd != savedPwd:
    print("Wrong password. Try again.")
    pwd = input("Enter a password:")
else:
    print("Logged in.")