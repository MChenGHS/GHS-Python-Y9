hourspernight = input("How many hours per night do you sleep? ")

# This line would not work
# hoursperweek = hourspernight * 7
# The result captured by the input, hourspernight, is a string. Mathematical operations cannot be applied to strings.

# Replace with this
hoursperweek = int(hourspernight) * 7

print("You sleep ", hoursperweek, " hours per week.")

# Additional task
hourspermonth = int(hourspernight) * 30
print("You sleep ", hourspermonth, " hours per month.")

hoursperyear = int(hourspernight) * 365
print("You sleep ", hoursperyear, " hours per year.")

days = hoursperyear / 24
print("That's equivalent to ", days, " days in a year!")