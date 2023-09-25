age = int(input("How old are you? "))
if age < 5:
  print("The museum is free for you.")
else:
  # This is another way to achieve multi-way branching, by using another if-else within an if-else
  if age > 16:
    print("Please pay £5.")
  else:
    print("Please pay £3.")