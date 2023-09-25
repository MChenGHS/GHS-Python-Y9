sname = input("What is your surname? ")
fname = input("What is your first name? ")
year = input("On which year were you born? ")

fname_initial = fname[0]
year_last = year[-2:]

print("Your user ID is:")
print(sname + fname_initial + year_last)
