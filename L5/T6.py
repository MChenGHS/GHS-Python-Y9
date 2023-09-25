# Currency rates accessed 21/09/23
rate_GBP_EUR = 1.15
rate_GBP_USD = 1.23
rate_GBP_JPY = 180

# Ask user the amount they have in GBP
domestic = float(input("Enter the amount in GBP: "))

# Check if the amount is correct
if domestic <= 0:
  print("You must have a positive amount to convert.")
else:
  # These code will only execute when the amount is positive
  # Present the user with options
  print("Select your currency: ")
  print("1 for GBP to EUR")
  print("2 for GBP to USD")
  print("3 for GBP to JPY")
  option = input()
  
  # Convert money depending on the user's chosen currency
  if option == "1":
    foreign = domestic * rate_GBP_EUR
  elif option == "2":
    foreign = domestic * rate_GBP_USD
  elif option == "3":
    foreign = domestic * rate_GBP_JPY
  else:
    # When the user didn't choose from 1, 2 or 3
    print("The choice is invalid.")
    foreign = -1 # Set an intentional impossible value to indicate that something went wrong
  
  if foreign > 0:
    # Code below now will only run if there's nothing wrong from above
    print("You'll have ", foreign, " in your chosen currency.")