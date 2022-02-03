import random
n=20
number=int((n*random.random())+1)
guess=0
while guess != number:
    guess=int(input("Enter the number: "))
    if guess>0:
        if guess>number:print("Number is too large!")
        elif guess<number:print("Number is too small!")
    else:print("Sorry, you lost the game!")
else:print('Congratulations! You won the game!')