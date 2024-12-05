import random

upper = int(input("Insert higher number: "))
lower = int(input("Insert lower number: "))

iteraction = 0
done = False

if upper > lower:
    choice = random.randint(lower,upper)
    while not done:
        number = int(input("Guess the number: "))
        iteraction += 1
        if number < choice:
            print("Your number is lower")
        elif number > choice:
            print("Your number is higher")
        elif number == choice:
            print("Number guessed")
            done = True
    print(f"Finished, the number was {choice} ")
    print(f"Iteraction:{iteraction}")
else:
    print("Wrong values")