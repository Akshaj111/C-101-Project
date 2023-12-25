import random
import os 
import 
response = input("Press y if you want to roll the die, n if not.")
no = random.randint(1,6)

if response == 'y':
    print(no)
elif response == 'n':
    os.system('cls')
    print("Thanks for trying out the die rolling simulator!")