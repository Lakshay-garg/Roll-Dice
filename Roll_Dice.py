import random

max_value = 6
min_value = 1

roll_again = "yes".lower()

while roll_again == "yes" or roll_again == "y":
    print("Rolling the Dices")
    print("The Values are")

    # rolling the first dice
    print(random.randint(min_value, max_value))

    # rolling the second dice
    print(random.randint(min_value, max_value))

    roll_again = input("Type yes to roll the dice again :")