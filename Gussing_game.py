import random
from random import randint

ran = random.randint(1,10)

while True:
    guess = int(input("Enter your guess between 1 to 10 : "))

    if guess > ran:
        print("Guess is large : ")
    elif guess < ran:
        print(" Guess is small : ")
    elif guess == ran:
        print("Congratulation you have chose the right guess !!! ")
        rep = input("Do you want to continue Y/N :")
        if rep == "Y" or rep == "y":
            from random import randint
            ran=random.randint
        else:
            break
