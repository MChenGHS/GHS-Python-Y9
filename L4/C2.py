speed = int(input("Speed of the vehicle? "))
if speed < 30: # Decision 1
  print("You'll be fine.") # Branch A
elif speed < 40: # Decision 2
  print("Watch your speed!") # Branch B
else:
  print("You'll be fined.") # Branch C

# If speed is below 30, then the program will go and execute branch A without checking the rest.
# Only if speed is 30 or more will decision 2, branch B and C be checked.
# So when the code reaches decision 2 the speed is definitely 30 or above.
# Now we only need to check if the speed is lower than 40 to determine between branch B and C.