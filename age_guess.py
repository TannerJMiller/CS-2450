import random
# This program is a simple age guessing game. It will ask the user for their name and then try to guess their age by randomly selecting a number between 15 and 40. The user will respond with 'y' for yes or 'n' for no, and the program will continue guessing until it gets the correct age.
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