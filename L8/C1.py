import random # See L7/T2-3.py for more information about this

chances = 3 # Make it a variable at the top of the program, so you can change this easily later

attempt = 0 # Initalise the counter variable
number = random.randint(1,500)
guess = int(input("Take a chance: "))
attempt = attempt + 1

while guess != number and attempt < chances:
    # Now the program will leave the while loop under 2 cases:
    # A) guess equals to number, meaning the player hit the jackpot
    # B) attempt is no longer smaller than chances, meaning the player has exhausted their chances
    attempt = attempt + 1
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Take another chance: "))

if guess == number:
    # Case A
    print("Bingo!")
else:
    # Case B
    print("You've exhausetd your chances.")