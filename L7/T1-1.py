answer = input("Quelle est la capitale de la France?")
answer = answer.title()

while answer != "Paris":
    answer = input("Ce n'est pas capitale de la France.")
    answer = answer.title()
print("Très bien")