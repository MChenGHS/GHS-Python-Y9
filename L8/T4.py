import random # See L7/T2-3.py for more information about this

number = random.randint(1,500)
guess = int(input("Take a chance: "))

while guess != number:
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Take another chance: "))
    
print("Bingo!")