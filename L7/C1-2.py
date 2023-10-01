count = 0 # Initalise the counter
answer = input("Quelle est la capitale de la France?")
answer = answer.title()
count = count + 1 # Include the first attempt

while answer != "Paris":
    count = count + 1 # Add 1 after each failed attempt
    answer = input("Ce n'est pas capitale de la France.")
    answer = answer.title()
print("Vous avez fait", count, " tentatives.")

if count < 6:
    print("Trés bien!")
elif: count < 8:
    print("Bien.")
else:
    print("C'est pas bon.")