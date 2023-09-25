temp = int(input("Enter temperature: "))

if temp >= 0 and temp <= 5:
  print("It's freezing!")
elif temp >= 6 and temp <= 10:
  print("Pretty chilly!")
elif temp >= 11 and temp <= 12:
  print("Could be warmer")
elif temp >= 13 and temp <= 20:
  print("It is bearable")
elif temp >= 21 and temp <= 25:
  print("Is this summer?")
elif temp >= 26 and temp <= 31:
  print("Where is the suntan oil?")
elif temp >= 30 and temp <= 34:
  print("Tropical and lazy")
else:
  print("Not a habitable temperaure")
