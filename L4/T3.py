password = input("Please set a password")
print("Password set.")

attempt = input("Enter your password: ")
if attempt == password: # Use '==' to check if left equals to right
  print("Unlocked")
else:
  print("Wrong password")