import random

correct_cup = random.randint(1, 3)
input_cup = input("Choose a cup: ")

if correct_cup == int(input_cup):
    print("You won.")
else:
    print("You lost.")

print("The ball was in cup " + str(correct_cup))