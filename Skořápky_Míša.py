import random

cup_list = [0, 0, 0]
input_cup = input("Zadej hodnotu 1-3: ")
cup_list[random.randint(0, 1)] = 1
order_of_cup = int(input_cup) - 1

if cup_list[order_of_cup] == 1:
    print("Vyhrál si")
else:
    print("prohrál si")
print(cup_list)
