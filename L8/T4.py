import random

number = random.randint(500)
guess = int(input("Take a chance: "))

while guess != 23:
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Take another chance: "))
    
print("Bingo!")