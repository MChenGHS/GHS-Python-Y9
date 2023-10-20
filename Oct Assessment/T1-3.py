num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
userSum = num1 + num2 + num3
checkSum = 1230
if userSum != checkSum:
    print("Invalid credentials.")
else:
    print("Logged in.")