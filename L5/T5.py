total = int(input("Enter the total: "))

if total > 100:
  service = 0
else:
  service = total * 0.1

print("You'll need to pay £", total + service, " for your meal.")
