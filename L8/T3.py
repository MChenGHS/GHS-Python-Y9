number = 23
guess = int(input("Take a chance: "))

if guess < number:
    print("Too low")
elif guess > number:
    print("Too high")
else:
    print("Bingo!")