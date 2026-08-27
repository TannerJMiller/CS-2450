import random
# This program is a simple age guessing game. It will ask the user for their name and then try to guess their age by randomly selecting a number between 15 and 40. The user will respond with 'y' for yes or 'n' for no, and the program will continue guessing until it gets the correct age.
def guess_age():
    name = input("Enter your name: ")
    got_age = False
    c = 15
    d = 40
    while not got_age:
        b = random.randint(c, d)
        a = input(f"Is your age {b}? (y/n): ")
        if a.lower() == 'y':
            print(f"Great! I guessed your age, {name}. You are {b} years old.")
            got_age = True
        else:
            e =input("Rats! is your age higher or lower than my guess? (h/l): ")
            if e == "h":
                c = b
            elif e == "l":
                d = b


guess_age()