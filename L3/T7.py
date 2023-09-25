name = input("What's your name? ")
operator = input("Who is the operator of your phone? ")
# Note that call minutes might not be a whole number
call = float(input("How many minutes have you called this month? "))
text = int(input("How many texts have you sent this month? "))

bill = call * 0.1 + text * 0.05
print(name, ", your bill before VAT is £", bill)
print("Your bill after VAT is £", bill * 1.2)