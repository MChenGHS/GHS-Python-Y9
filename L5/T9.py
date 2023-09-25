retail_price = float(input("What's the retail price? "))
code = input("What's the customer's code? ")

if code == "A":
  retail_price = retail_price * 0.7
elif code == "B":
  retail_price = retail_price * 0.8
elif code == "C":
  retail_price = retail_price * 0.92
elif code == "D":
  retail_price = retail_price * 0.95

print("The total payable is £", retail_price)