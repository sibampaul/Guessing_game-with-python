import random
from random import randint

ran = random.randint(1,10)


while True:
  guess = int(input("Guess a number Between 1 to 10 : "))
  if guess >10 :
    print("wrong Guess Please chose bet")
  elif guess > ran:
    print("guess is large")
  elif guess < ran:
    print("guess is small")
  elif guess == ran:
    print("congratulation your guess is right !!!")
    cont = input("Do you want to continue Y/N ?? : ")
    if cont == "Y" or cont == "y":
      from random import randint
      ran = random.randint(1,10)
    else:
      break
