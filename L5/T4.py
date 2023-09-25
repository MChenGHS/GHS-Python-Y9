salary = int(input("Enter the salary: "))

if salary > 100:
  tax = 9 + (salary - 100) * 0.12
else:
  tax = salary * 0.09

print("You'll need to pay £", tax, " in tax.")
print("You'll have £", salary - tax, " to take home.")
