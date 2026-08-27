import random

def guess_age():
    name = input("Enter your name: ")
    got_age = False
    while not got_age:
        b = random.randint(15, 40)
        a = input(f"Is your age {b}? (y/n): ")
        if a.lower() == 'y':
            print(f"Great! I guessed your age, {name}. You are {b} years old.")
            got_age = True
        else:
            print("Rats!")

guess_age()