import random

randomNumber = random.randrange(1,11)

for i in range(3):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < randomNumber: 
        print("Too low!")
    elif guess > randomNumber:     
        print("Too high!")
    elif guess == randomNumber:  
        print("Correct!")
        break
