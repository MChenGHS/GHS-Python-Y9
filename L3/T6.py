p1 = int(input("How many 1p do you have? "))
p2 = int(input("How many 2p do you have? "))
p5 = int(input("How many 5p do you have? "))
p10 = int(input("How many 10p do you have? "))
p20 = int(input("How many 20p do you have? "))
p50 = int(input("How many 50p do you have? "))
p100 = int(input("How many £1 do you have? "))

# Calculate sum in pence
sum = p1 * 1 + p2 * 2 + p5 * 5 + p10 * 10 + p20 * 20 + p50 * 50 + p100 * 100
# Divide by 100 so the value would be in pounds
sum = sum / 100

print("You have £", sum, " in total.")
