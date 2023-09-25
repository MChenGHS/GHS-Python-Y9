mark = int(input("Enter student's mark: "))
if mark < 50:
  print("Fail") # Marks between 0 and 49 goes here
elif mark > 60:
  print("Plus") # Marks between 61 and 100 goes here
else:
  print("Pass") # Marks between 50 and 60 goes here