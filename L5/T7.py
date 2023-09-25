allowed = True # This value is True by default, when the passenger fails any check it will be set to False.

# Checking prohibited
print("Do you have any prohibited items? ")
prohibited = input("Y for yes, N for no ")
if prohibited == "Y":
  allowed = False # The passenger failed this check

# Checking weight
weight = float(input("What's the weight of your luggage? "))
if weight > 22:
  allowed = False # The passenger failed this check

if allowed: # Essentially the same as 'if allowed == True'
  print("Welcome abroad.") # Meaning passenger passed all checks
else:
  print("Sorry, you cannot board.") # Meaning passenger failed one or more checks