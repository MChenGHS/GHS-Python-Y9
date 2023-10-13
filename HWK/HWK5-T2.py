import random
count6 = 0
numberOfThrows = 0
while numberOfThrows < 6000:
    throw = random.randint(1,6)
    numberOfThrows = numberOfThrows + 1
    if throw == 6:
        count6 = count6 + 1
print("Number of sixes",count6)
