# Write a Python program that generates a
# random number between 1 and 100. The
# user should then try to guess the number.
# The program should provide hints such as
# "too high" or "too low" until the correct
# number is guessed.

import random

computer=random.randint(1,100)

while(True):
    user=int(input("Guess the number:-"))
    if(user==computer):
        print("Congratulation! You Guess Right Number")
    elif(user>50):
        print("It is to High")
    elif(user<50):
        print("It is too Low")
    else:
        print("You Guess Wrong Number")