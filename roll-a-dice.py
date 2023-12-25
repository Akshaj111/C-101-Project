import random
import os 

response = input("Press y if you want to roll the die, n if not.")
no = random.randint(1,6)

while True:
    if response == 'y':
        print(no)
    elif response == 'n':
        os.system('cls')
        print("Thanks for trying out the die rolling simulator!")
        break