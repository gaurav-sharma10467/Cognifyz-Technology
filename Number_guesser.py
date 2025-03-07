# Create a number guessing game where the
# program generates a random number
# between a specified range, and the user tries
# to guess it. Provide feedback to the user if
# their guess is too high or too low.

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